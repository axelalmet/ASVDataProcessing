import os as os
import csv

# Get the current working directory
cwd = os.getcwd() + '/'

# Initialise dictionaries to store each sequence
typeCounts = {}
phylaGeneraCounts = {}
phylaCounts = {}
phylaLists = {}

genusCount = 0
phylumCount = 0
asvCount = 0
naCount = 0

# Store the original ASVs first
inputFile = 'ForPhylumGenusASVTable.csv'
with open(cwd + inputFile) as taxasFile:

    # Read in the files as dictionaries
    taxaDictReader = csv.DictReader(taxasFile)

    # Store the different type counts and also the different phyla/genera
    for row in taxaDictReader:

        asv_type = row["Type"]
        phylum = row["Phylum"]
        genus = row["Genus"]

        # Store the ASV types
        if asv_type not in typeCounts: # If you haven't stored this ASV type into the dictionary

            typeCounts[asv_type] = 1
            asvCount += 1

        else: # Otherwise we can just update the count

            typeCounts[asv_type] += 1
            asvCount += 1

        # Store the phyla and also the dictionary of of genera and their counts
        if phylum not in phylaGeneraCounts:

            phyla_dict = {} # Initialise the dictionary
            phyla_dict[genus] = 1

            phylaGeneraCounts[phylum] = phyla_dict

            phylumCount += 1

            if genus != "NA":
                genusCount += 1

            if genus == "NA":
                naCount += 1

        else:

            phyla_dict = phylaGeneraCounts[phylum]

            if genus not in phyla_dict:

                phyla_dict[genus] = 1

                if genus != "NA":
                    genusCount += 1

                if genus == "NA":
                    naCount += 1

            else:
                phyla_dict[genus] += 1

            phylaGeneraCounts[phylum] = phyla_dict

        # Update the list of genera per phyla and the phylum counts
        if phylum not in phylaCounts:
            phylaCounts[phylum] = 1
        else:
            phylaCounts[phylum] += 1

        if phylum not in phylaLists:

            phylaLists[phylum] = [genus]

        else:

            genus_list = phylaLists[phylum]

            if (genus not in genus_list):
                genus_list.append(genus)
                phylaLists[phylum] = genus_list

    print([phylumCount, genusCount, naCount])

    genusCount = 0
    genusList = []
    genusDict = {}

    for phylum in phylaGeneraCounts:
        genus_dict = phylaGeneraCounts[phylum]
        for genus in genus_dict:
            if genus != "NA":
                if genus not in genusDict:
                    genusDict[genus] = 1
                else:
                    print([phylum, genus])
                    genusDict[genus] += 1
                if genus not in genusList:
                    genusList.append(genus)

    repeatedGenera = {}

    for genus in genusDict:
        if genusDict[genus] > 1:
            repeatedGenera[genus] = [phylum for phylum in phylaGeneraCounts if genus in phylaGeneraCounts[phylum]]

    # print([len(genusList), len(genusDict)])
    print(repeatedGenera)
    print(len(repeatedGenera))

    typeCountsFileName = 'TypeCounts.csv'
    phylaGeneraCountsFileName = 'PhylaGeneraCounts.csv'
    phylaSortedGeneraCountsFileName = 'PhylaSortedGeneraCounts.csv'

    # Store these different counts in new tables
    with open(cwd + typeCountsFileName, 'w') as typeCountsFile, open(cwd + phylaGeneraCountsFileName, 'w') as phylaGeneraCountsFile, \
        open(cwd + phylaSortedGeneraCountsFileName, 'w') as phylaSortedFile:

        # Create the file for the asv types and their counts
        typeCountsHeaders = ['Type', 'Count']
        typeFileWriter = csv.DictWriter(typeCountsFile, delimiter=",", fieldnames=typeCountsHeaders)
        typeFileWriter.writeheader()

        # Create the file for the phyla and genera counts
        phylaGeneraCountsHeaders = ['Phylum', 'Genus', 'Number of ASVs']
        phylaGeneraFileWriter = csv.DictWriter(phylaGeneraCountsFile, delimiter=",", fieldnames=phylaGeneraCountsHeaders)
        phylaGeneraFileWriter.writeheader()

        # Create the file for the phyla and sorted genera counts
        phylaSortedFileWriter = csv.DictWriter(phylaSortedFile, delimiter=",", fieldnames=phylaGeneraCountsHeaders)
        phylaSortedFileWriter.writeheader()

        # Write the files now!
        for asv_type in typeCounts:
            line = {'Type': asv_type, 'Count': typeCounts[asv_type]}
            typeFileWriter.writerow(line)

        for phylum in phylaGeneraCounts:

            genus_counts = phylaGeneraCounts[phylum]

            for genus in genus_counts:
                line = {'Phylum': phylum, 'Genus': genus, 'Number of ASVs': genus_counts[genus]}

                phylaGeneraFileWriter.writerow(line)

        for phylum in phylaLists:

            list_of_genera = phylaLists[phylum]
            list_of_genera.sort() # Sort the list in alphabetical order

            genera = ''

            na_string = ''

            for genus in list_of_genera:

                if genus == 'NA': # We count how many NA genuses there are per phylum
                    na_count = phylaGeneraCounts[phylum][genus]
                    na_string = genus + ' (' + str(na_count) + ')'

                if genera == '': # Initialise the string if this is the first word
                    if genus != 'NA':
                        genera += genus
                else: # We need to add a comma
                    if genus != 'NA':
                        genera += ', ' + genus

            if na_string != '':
                if genera == '':
                    genera += na_string
                else:
                    genera += ', ' + na_string

            phylum_count = phylaCounts[phylum] # Get the number of ASVs correspondign tot hsi phylum
            line = {'Phylum': phylum, 'Genus': genera, 'Number of ASVs': phylum_count}

            phylaSortedFileWriter.writerow(line)