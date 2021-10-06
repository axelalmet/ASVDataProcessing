import os as os
import csv

# Get the current working directory
cwd = os.getcwd() + '/'

# Initialise dictionaries to store each sequence
FemaleSeqs = {}
MaleSeqs = {}
EjacSeqs = {}
FemaleCloacaSeqs = {}
MaleCloacaSeqs = {}
FemaleColonSeqs = {}
MaleColonSeqs = {}
FemaleFaecesSeqs = {}
MaleFaecesSeqs = {}

SeqsList = []
allSeqs = {}
TypeCounts = {} # We will store all possible combinations of types and how many there are in this

FemaleASVs = {}
MaleASVs = {}
EjacASVs = {}
FemaleCloacaASVs = {}
MaleCloacaASVs = {}
FemaleColonASVs = {}
MaleColonASVs = {}
FemaleFaecesASVs = {}
MaleFaecesASVs = {}
TotalASVs = {}

# Initialise these different counts as a sanity check
femaleCount = 0 # Female reproductive tract
maleCount = 0 # Male reproductive tract
ejacCount = 0 # Ejaculate data
femaleCloacaCount = 0 # Female cloaca
maleCloacaCount = 0 # Male cloaca   
femaleColonCount = 0 # Female colon
maleColonCount = 0 # Male colon
femaleFaecesCount = 0 # Female faeces
maleFaecesCount = 0 # Male faeces

# Define the keys we will use to indicate different data types
femaleKey = 'F'
maleKey = 'M'
ejaculateKey = 'E'
femaleCloacaKey = 'C'
maleCloacaKey = 'G'
femaleColonKey = 'O'
maleColonKey = 'L'
femaleFaecesKey = 'S'
maleFaecesKey = 'P'

# Define the intput file names (replace these with your own)
femaleInputFileName = '/138FemalesTRACT.csv'
maleInputFileName = '/138MalesTRACT.csv'
ejaculatesInputFileName = '/138MalesEJACULATES.csv'
femaleCloacaInputFileName = '/138FemalesCLOACA.csv'
maleCloacaInputFileName = '/138MalesCLOACA.csv'
femaleColonInputFileName = '/138FemalesCOLON.csv'
maleColonInputFileName = '/138MalesCOLON.csv'
femalesFaecesInputFileName = '/138FemalesFAECES.csv'
maleFaecesInputFileName = '/138MalesFAECES.csv'

# Store the original ASVs first
with open(cwd + femaleInputFileName) as femaleFile, open(cwd + maleInputFileName) as maleFile, \
    open(cwd + ejaculatesInputFileName) as ejacFile, \
    open(cwd + femaleCloacaInputFileName) as femaleCloacaFile, open(cwd + maleCloacaInputFileName) as maleCloacaFile,\
    open(cwd + femaleColonInputFileName) as femaleColonFile, open(cwd + maleColonInputFileName) as maleColonFile, \
    open(cwd + femalesFaecesInputFileName) as femaleFaecesFile, open(cwd + malesFaecesInputFileName) as maleFaecesFile:

    # Read in the files as dictionaries
    femaleDictReader = csv.DictReader(femaleFile)
    maleDictReader = csv.DictReader(maleFile)
    ejacDictReader = csv.DictReader(ejacFile)
    femaleCloacaDictReader = csv.DictReader(femaleCloacaFile)
    maleCloacaDictReader = csv.DictReader(maleCloacaFile)
    femaleColonDictReader = csv.DictReader(femaleColonFile)
    maleColonDictReader = csv.DictReader(maleColonFile)
    femaleFaecesDictReader = csv.DictReader(femaleFaecesFile)
    maleFaecesDictReader = csv.DictReader(maleFaecesFile)

    # Store the different sequences
    for row in femaleDictReader:
        FemaleSeqs[row["Sequence"]] = row
        if row["Sequence"] not in allSeqs: # We construct the union of all sequences and their types
            allSeqs[row["Sequence"]] = [femaleKey]

    for row in maleDictReader:
        MaleSeqs[row["Sequence"]] = row
        if row["Sequence"] not in allSeqs: # If this sequence hasn't been considered
            allSeqs[row["Sequence"]] = [maleKey]
        else: # Else add it to the current list of types for the dictionary
            current_list = allSeqs[row["Sequence"]]
            current_list.append(maleKey)
            allSeqs[row["Sequence"]] = current_list

    for row in ejacDictReader:
        EjacSeqs[row["Sequence"]] = row
        if row["Sequence"] not in allSeqs: # If this sequence hasn't been considered
            allSeqs[row["Sequence"]] = [ejaculateKey]
        else: # Else add it to the current list of types for the dictionary
            current_list = allSeqs[row["Sequence"]]
            current_list.append(ejaculateKey)
            allSeqs[row["Sequence"]] = current_list

    for row in femaleCloacaDictReader:
        FemaleCloacaSeqs[row["Sequence"]] = row
        if row["Sequence"] not in allSeqs: # If this sequence hasn't been considered
            allSeqs[row["Sequence"]] = [femaleCloacaKey]
        else: # Else add it to the current list of types for the dictionary
            current_list = allSeqs[row["Sequence"]]
            current_list.append(femaleCloacaKey)
            allSeqs[row["Sequence"]] = current_list

    for row in maleCloacaDictReader:
        MaleCloacaSeqs[row["Sequence"]] = row
        if row["Sequence"] not in allSeqs: # If this sequence hasn't been considered
            allSeqs[row["Sequence"]] = [maleCloacaKey]
        else: # Else add it to the current list of types for the dictionary
            current_list = allSeqs[row["Sequence"]]
            current_list.append(maleCloacaKey)
            allSeqs[row["Sequence"]] = current_list

    for row in femaleColonDictReader:
        FemaleColonSeqs[row["Sequence"]] = row
        if row["Sequence"] not in allSeqs: # If this sequence hasn't been considered
            allSeqs[row["Sequence"]] = [femaleColonKey]
        else: # Else add it to the current list of types for the dictionary
            current_list = allSeqs[row["Sequence"]]
            current_list.append(femaleColonKey)
            allSeqs[row["Sequence"]] = current_list

    for row in maleColonDictReader:
        MaleColonSeqs[row["Sequence"]] = row
        if row["Sequence"] not in allSeqs: # If this sequence hasn't been considered
            allSeqs[row["Sequence"]] = [maleColonKey]
        else: # Else add it to the current list of types for the dictionary
            current_list = allSeqs[row["Sequence"]]
            current_list.append(maleColonKey)
            allSeqs[row["Sequence"]] = current_list

    for row in femaleFaecesDictReader:
        FemaleFaecesSeqs[row["Sequence"]] = row
        if row["Sequence"] not in allSeqs: # If this sequence hasn't been considered
            allSeqs[row["Sequence"]] = [femaleFaecesKey]
        else: # Else add it to the current list of types for the dictionary
            current_list = allSeqs[row["Sequence"]]
            current_list.append(femaleFaecesKey)
            allSeqs[row["Sequence"]] = current_list

    for row in maleFaecesDictReader:
        MaleFaecesSeqs[row["Sequence"]] = row
        if row["Sequence"] not in allSeqs: # If this sequence hasn't been considered
            allSeqs[row["Sequence"]] = [maleFaecesKey]
        else: # Else add it to the current list of types for the dictionary
            current_list = allSeqs[row["Sequence"]]
            current_list.append(maleFaecesKey)
            allSeqs[row["Sequence"]] = current_list

    # Store these sequence dictionaries in a list 
    SeqsList = [FemaleSeqs, MaleSeqs, EjacSeqs, FemaleCloacaSeqs, MaleCloacaSeqs, FemaleColonSeqs, MaleColonSeqs, FemaleFaecesSeqs, MaleFaecesSeqs]

    print(len(allSeqs), len(FemaleSeqs), len(MaleSeqs), len(EjacSeqs), len(FemaleCloacaSeqs), len(MaleCloacaSeqs), len(FemaleColonSeqs), len(MaleColonSeqs), len(FemaleFaecesSeqs), len(MaleFaecesSeqs))

    # We need to also consider all the possible subsets
    for seq in allSeqs:
        seqTypes = allSeqs[seq] # Get the list of types
        type_ID = ''
        # We will store the type as one concatenated string
        type_ID = type_ID.join(seqTypes)
        TypeCounts[type_ID] = 0 # Initialise the count

    print(len(TypeCounts))

    # Create the new file csvs
    femaleOutputFileName = './FREPASV138.csv'
    maleOutputFileName = '/MREPASV138.csv'
    ejaculatesOutputFileName = '/EjaculateASV138.csv'
    femaleCloacaOutputFileName = '/FCloacaASV138.csv'
    maleCloacaOutputFileName = '/MCloacaASV138.csv'
    femaleColonOutputFileName = '/FCOLASV138.csv'
    maleColonOutputFileName = '/MCOLASV138.csv'
    femalesFaecesOutputFileName = '/FFECASV138.csv'
    maleFaecesOutputFileName = '/MFECASV138.csv'
    combinedOutputFileName = '/138CombinedASV.csv'

    with open(cwd + femaleOutputFileName, 'w') as femaleNewFile, open(cwd + maleOutputFileName, 'w') as maleNewFile, \
        open(cwd + ejaculatesOutputFileName, 'w') as ejacNewFile, \
        open(cwd + femaleCloacaOutputFileName, 'w') as femaleCloacaNewFile, open(cwd + maleCloacaOutputFileName, 'w') as maleCloacaNewFile,\
        open(cwd + femaleColonOutputFileName, 'w') as femaleColonNewFile, open(cwd + maleColonOutputFileName, 'w') as maleColonNewFile, \
        open(cwd + femalesFaecesOutputFileName, 'w') as femaleFaecesNewFile, open(cwd + maleFaecesOutputFileName, 'w') as maleFaecesNewFile, \
        open(cwd + combinedOutputFileName, 'w') as totalNewFile:

        # Create the new row ID
        headerNames = femaleDictReader.fieldnames
        headerNames.append('ASVID')

        # Write the column names to the new csv files
        newFemaleFileWriter = csv.DictWriter(femaleNewFile, delimiter=",", fieldnames=headerNames)
        newFemaleFileWriter.writeheader()

        newMaleFileWriter = csv.DictWriter(maleNewFile, delimiter=",", fieldnames=headerNames)
        newMaleFileWriter.writeheader()

        newEjacFileWriter = csv.DictWriter(ejacNewFile, delimiter=",", fieldnames=headerNames)
        newEjacFileWriter.writeheader()

        newFemaleCloacaFileWriter = csv.DictWriter(femaleCloacaNewFile, delimiter=",", fieldnames=headerNames)
        newFemaleCloacaFileWriter.writeheader()

        newMaleCloacaFileWriter = csv.DictWriter(maleCloacaNewFile, delimiter=",", fieldnames=headerNames)
        newMaleCloacaFileWriter.writeheader()

        newFemaleColonFileWriter = csv.DictWriter(femaleColonNewFile, delimiter=",", fieldnames=headerNames)
        newFemaleColonFileWriter.writeheader()

        newMaleColonFileWriter = csv.DictWriter(maleColonNewFile, delimiter=",", fieldnames=headerNames)
        newMaleColonFileWriter.writeheader()

        newFemaleFaecesFileWriter = csv.DictWriter(femaleFaecesNewFile, delimiter=",", fieldnames=headerNames)
        newFemaleFaecesFileWriter.writeheader()

        newMaleFaecesFileWriter = csv.DictWriter(maleFaecesNewFile, delimiter=",", fieldnames=headerNames)
        newMaleFaecesFileWriter.writeheader()

        # Add an extra header for the total names
        headerNames.append('Type')

        newTotalFileWriter = csv.DictWriter(totalNewFile, delimiter=",", fieldnames=headerNames)
        newTotalFileWriter.writeheader()

        for seq in allSeqs:
            seqTypes = allSeqs[seq] # Get all the type IDs

            # Let's construct the ASV ID now
            joinedTypes = ''
            joinedTypes = joinedTypes.join(seqTypes) # This constructs a concatenated string of all the possible types
            asvCount = TypeCounts[joinedTypes] + 1 # Get the ASV count
            TypeCounts[joinedTypes] = asvCount # Need to update this for the next sequence

            asvID = 'ASV' + joinedTypes + str(asvCount)

            # Now let's figure out where to write the sequence info to
            sequenceInfo = [] # We need to initialise this to write it to the total ASV file
            if femaleKey in seqTypes: # Female reproductive

                sequenceInfo = FemaleSeqs[seq] # Get the sequence
                sequenceInfo['ASVID'] = asvID # Add the ASV ID to the list
                newFemaleFileWriter.writerow(sequenceInfo) # Write the row

            elif maleKey in seqTypes: # Male reproductive

                sequenceInfo = MaleSeqs[seq] # Get the sequence
                sequenceInfo['ASVID'] = asvID # Add the ASV ID to the list
                newMaleFileWriter.writerow(sequenceInfo) # Write the row

            elif ejaculateKey in seqTypes: # Ejaculate 
            
                sequenceInfo = EjacSeqs[seq] # Get the sequence
                sequenceInfo['ASVID'] = asvID # Add the ASV ID to the list
                newEjacFileWriter.writerow(sequenceInfo) # Write the row

            elif femaleCloacaKey in seqTypes: # Cloaca 

                sequenceInfo = FemaleCloacaSeqs[seq] # Get the sequence
                sequenceInfo['ASVID'] = asvID # Add the ASV ID to the list
                newFemaleCloacaFileWriter.writerow(sequenceInfo) # Write the row
                
            elif maleCloacaKey in seqTypes: # Cloaca 

                sequenceInfo = MaleCloacaSeqs[seq] # Get the sequence
                sequenceInfo['ASVID'] = asvID # Add the ASV ID to the list
                newMaleCloacaFileWriter.writerow(sequenceInfo) # Write the row

            elif femaleColonKey in seqTypes: # Female Colon

                sequenceInfo = FemaleColonSeqs[seq] # Get the sequence
                sequenceInfo['ASVID'] = asvID # Add the ASV ID to the list
                newFemaleColonFileWriter.writerow(sequenceInfo) # Write the row

            elif maleColonKey in seqTypes: # Male Colon

                sequenceInfo = MaleColonSeqs[seq] # Get the sequence
                sequenceInfo['ASVID'] = asvID # Add the ASV ID to the list
                newMaleColonFileWriter.writerow(sequenceInfo) # Write the row

            elif femaleFaecesKey in seqTypes: # Female faeces

                sequenceInfo = FemaleFaecesSeqs[seq] # Get the sequence
                sequenceInfo['ASVID'] = asvID # Add the ASV ID to the list
                newFemaleFaecesFileWriter.writerow(sequenceInfo) # Write the row

            elif maleFaecesKey in seqTypes: # Male faeces

                sequenceInfo = MaleFaecesSeqs[seq] # Get the sequence
                sequenceInfo['ASVID'] = asvID # Add the ASV ID to the list
                newMaleFaecesFileWriter.writerow(sequenceInfo) # Write the row
    
            # We now write this row to the total ASVs, taking care to also annotate the type
            sequenceInfo['Type'] = joinedTypes
            newTotalFileWriter.writerow(sequenceInfo)
