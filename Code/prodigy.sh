#!/bin/bash

# Check if results.csv exists, if not, create it and add a header
if [ ! -f prodigy_data.csv ]; then
    touch prodigy_data.csv
    echo "pdbid,selection,intermolecular_contacts,charged_charged_contacts,charged_polar_contacts,charged_apolar_contacts,polar_polar_contacts,apolar_polar_contacts,apolar_apolar_contacts,percentage_apolar_nis,percentage_charged_nis,binding_affinity,dissociation_constant" >> prodigy_data.csv
fi

# Input parameters
pdb_file=$1
selection=$2

# Run Prodigy and capture the output
output=$(prodigy $pdb_file --selection $selection)

# Parse the output to extract numerical data
pdbid=$(echo "$output" | grep "Parsed structure file" | awk '{print $5}')
intermolecular_contacts=$(echo "$output" | grep "No. of intermolecular contacts" | awk '{print $NF}')
charged_charged_contacts=$(echo "$output" | grep "No. of charged-charged contacts" | awk '{print $NF}')
charged_polar_contacts=$(echo "$output" | grep "No. of charged-polar contacts" | awk '{print $NF}')
charged_apolar_contacts=$(echo "$output" | grep "No. of charged-apolar contacts" | awk '{print $NF}')
polar_polar_contacts=$(echo "$output" | grep "No. of polar-polar contacts" | awk '{print $NF}')
apolar_polar_contacts=$(echo "$output" | grep "No. of apolar-polar contacts" | awk '{print $NF}')
apolar_apolar_contacts=$(echo "$output" | grep "No. of apolar-apolar contacts" | awk '{print $NF}')
percentage_apolar_nis=$(echo "$output" | grep "Percentage of apolar NIS residues" | awk '{print $NF}')
percentage_charged_nis=$(echo "$output" | grep "Percentage of charged NIS residues" | awk '{print $NF}')
binding_affinity=$(echo "$output" | grep "Predicted binding affinity" | awk '{print $NF}')
dissociation_constant=$(echo "$output" | grep "Predicted dissociation constant" | awk '{print $NF}')
selection=$(echo "$selection" | sed 's/,//g')
# CSV output format
echo "$pdbid,$selection,$intermolecular_contacts,$charged_charged_contacts,$charged_polar_contacts,$charged_apolar_contacts,$polar_polar_contacts,$apolar_polar_contacts,$apolar_apolar_contacts,$percentage_apolar_nis,$percentage_charged_nis,$binding_affinity,$dissociation_constant" >> prodigy_data.csv