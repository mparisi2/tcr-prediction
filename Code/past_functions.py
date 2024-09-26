# def kernel_pca_scatter(data, data_values, i, j, kernel='linear'):
#     gamma = 0.05
#     kpca = KernelPCA(n_components=max(i, j) + 1, kernel=kernel, gamma=gamma)
#     X_kpca = kpca.fit_transform(data_values.values)

#     data[f'PCA{i}'] = X_kpca[:, i]
#     data[f'PCA{j}'] = X_kpca[:, j]
#     # data['label'] = data['label'].astype(str)
#     fig = px.scatter(data,
#                      x=f'PCA{i}',
#                      y=f'PCA{j}',
#                      color='label',
#                      color_discrete_sequence=['red', 'blue'],
#                      title=f'{kernel}PCA Training Data(PCA{i+1} vs PCA{j+1}) gamma = {gamma}',
#                      labels={f'PCA{i}': f'PCA{i+1}', f'PCA{j}': f'PCA{j+1}'},
#                      width=600,
#                      height=600)
#     directory = f'Data_Analysis_png/min_Kpca_{kernel}_binding'
#     if not os.path.exists(directory):
#         os.makedirs(directory)
#     fig.write_image(f'{directory}/PCA{i}_vs_PCA{j}.png')

# def spectral_embedding_scatter(data, data_values, i, j, affinity='nearest_neighbors', gamma=None, n_neighbors=5):
#     n_components = max(i, j) + 1
#     se = SpectralEmbedding(n_components=n_components, affinity=affinity, gamma=gamma, n_neighbors=n_neighbors)
#     X_se = se.fit_transform(data_values.values)

#     data[f'SE1'] = X_se[:, i]
#     data[f'SE2'] = X_se[:, j]
    
#     fig = px.scatter(data,
#                      x='SE1',
#                      y='SE2',
#                      color='label',
#                      color_discrete_sequence=['red', 'blue'],
#                      title='Training data (Spectral Embedding)',
#                      labels={'SE1': f'SE{i+1}', 'SE2': f'SE{j+1}'},
#                      width=600,
#                      height=600)
    
#     # Ensure the directory exists
#     directory = 'Data_Analysis_png/max_spectral'
#     if not os.path.exists(directory):
#         os.makedirs(directory)
    
#     # Save the figure
#     fig.write_image(f'{directory}/SE{i}_vs_SE{j}.png')

    # pdbids = pd.read_csv('Code/csv/training_cancer.csv')['pdbid']
    # directory = 'Data/TCR3D_PDBfiles'
    # pdbid_chain_info = pd.read_csv('Data/TCR3D_MHCI_data/PDBID_chain_info_GOOD.csv')

    # for pdbid in pdbids.values:
    #     file_name = pdbid + '.pdb'
    #     full_path = os.path.join(directory, file_name)
    #     row = pdbid_chain_info[pdbid_chain_info['PDBID'] == pdbid]
    #     if not row.empty:
    #         TRA = row['TRA'].values[0]
    #         TRB = row['TRB'].values[0]
    #         PEP = row['PEP'].values[0]
    #         MHC = row['MHC'].values[0]
    #     selection = f'{TRA},{TRB} {PEP}'
    #     uts.run_prodigy(full_path, selection)


    # directory = 'Data/fromNick/output_pos_backup'
    # for subdir in os.listdir(directory):
    #     ranked0 = 'ranked_0.pdb'
    #     path = os.path.join(os.path.join(directory, subdir), ranked0)
    #     uts.run_prodigy(path, 'D,E C')

# pos = pd.read_csv('Code/csv/positives_TCR-pMHC_real.csv').drop(columns=['pdbid'], inplace=False)
# pos['label'] = 1
# neg = pd.read_csv('Code/csv/negatives_TCR-pMHC_sythetic.csv').drop(columns=['pdbid', 'selection'], inplace=False)
# neg['label'] = 0
# newpd = pd.concat([pos, neg], ignore_index=True).sample(frac=1, ignore_index=True)
# newpd.to_csv('Code/csv/TCR-pMHC_labeled_real.csv', index=False)



# json file is a dictionary of dictionaries
# json_keys = ['ranked_0', 'ranked_1', 'ranked_2', 'ranked_3', 'ranked_4']
# ranked_keys = ['ranking_confidence', 'plddt', 'ptm', 'iptm', 'tcr-pmhc_iptm', 'cdr3a_plddt', 'cdr3b_plddt']
# json_name = 'statistics.json'
# directory = 'Data/fromNick/data_new/output_pos_cancer_backup'
# json_csv_path = 'json_info.csv'
# for subdir in os.listdir(directory):
#     path = os.path.join(directory, subdir)
#     json_path = os.path.join(path, json_name)
#     with open(json_path, 'r') as file:
#         json_file = json.load(file)
#     for name in json_keys:
#         ranked_path = os.path.join(path, name + '.pdb')
#         uts.run_prodigy(ranked_path)



# ranked_keys = ['ranking_confidence', 'plddt', 'ptm', 'iptm', 'tcr-pmhc_iptm', 'cdr3a_plddt', 'cdr3b_plddt']
# directory = 'Data/fromNick/data_new/output_neg_cancer_backup'
# json_name = 'statistics.json'
# prod_path = 'prodigy_data.csv'
# final_df = pd.DataFrame()
# if os.path.exists(prod_path):
#     os.remove(prod_path)
# for subdir in os.listdir(directory):
#     if os.path.exists(prod_path):
#         os.remove(prod_path)
#     path = os.path.join(directory, subdir)
#     for i in range(5):
#         ranked_i = f'ranked_{i}'
#         pdb_path = os.path.join(path, ranked_i + '.pdb')
#         if os.path.exists(pdb_path):
#             uts.run_prodigy(pdb_path)
#             uts.run_prodigy(pdb_path, 'D,E A')
#             json_path = os.path.join(path, json_name)
#             with open(json_path, 'r') as file:
#                 json_file = json.load(file)
#             ranked_confidence = float(json_file[ranked_i][ranked_keys[0]])
#             add_or_append_column(prod_path, ranked_keys[0], ranked_confidence)

#     choice = choose_best_delta_g(prod_path)
#     if choice is not None:
#         new_row = remove_all_but_one(prod_path, choice)
#     else:
#         continue
#     final_df = pd.concat([final_df, new_row], ignore_index=True)

# final_df.to_csv('Code/csv/new_data/neg_tcr2_deltaP_confidence.csv', index=False)


# def add_or_append_column(csv_path:str, header:str, value:float):
#     if os.path.exists(csv_path):
#         df = pd.read_csv(csv_path)
#         if header not in df.columns:
#             df[header] = value
#         else:
#             df[header] = df[header].fillna(value)
#         df.to_csv(csv_path, index=False)

# def choose_best_delta_g(csv_path:str):
#     attributes = ['pdbid', 'selection', 'intermolecular_contacts',
#        'charged_charged_contacts', 'charged_polar_contacts',
#        'charged_apolar_contacts', 'polar_polar_contacts',
#        'apolar_polar_contacts', 'apolar_apolar_contacts',
#        'percentage_apolar_nis', 'percentage_charged_nis', 'binding_affinity',
#        'dissociation_constant', 'ranking_confidence']
#     threshold = 0.5
#     if os.path.exists(csv_path):
#         df = pd.read_csv(csv_path)
#     else:
#         return None
#     ranked_entries = []

#     unique_ranks = df[attributes[0]].unique()

#     for rank in unique_ranks:
#         rank_df = df[df[attributes[0]] == rank]

#         if len(rank_df) == 2:
#             try:
#                 TCR_pMHC = rank_df[attributes[11]].iloc[0]
#                 TCR_MHC = rank_df[attributes[11]].iloc[1]
#                 binding_diff = -(TCR_pMHC - TCR_MHC)
#             except Exception as e:
#                 print(e)
#                 print(TCR_pMHC, TCR_MHC)
#                 return None
#             ranking_confidence = rank_df[attributes[13]].iloc[0]

#             ranked_entries.append((rank, binding_diff, ranking_confidence))
    

#     sorted_entries = sorted(ranked_entries, key = lambda x: (x[1], x[2]), reverse=True)

#     for i in range(5):
#         if sorted_entries[i][2] > threshold:
#             return sorted_entries[i][0]
#         else:
#             continue

# def remove_all_but_one(csv_path:str, choice:str):
#     if os.path.exists(csv_path):
#         df = pd.read_csv(csv_path)
#     df = df[(df['pdbid'] == choice) & (df['selection'] == 'DE CA')]
#     return df