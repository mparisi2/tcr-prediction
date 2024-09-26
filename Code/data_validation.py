import pandas as pd
import os
import TCR_utils as uts
import plotly.express as px
from sklearn.decomposition import PCA
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from copy import deepcopy

class Validate:
    """generates various .png related to the datas feature Distribution, PCA loadings, correlation matrix of features, and 2 dimensional scatter plot of PCA on data.
    """

    def __init__(self, path:str, df:pd.DataFrame = None, pos_label:str = 'TCRmodel2_pos', neg_label:str = 'TCRmodel2_neg', name_index = 2) -> None:
        """
        Args:
            path (str): .csv file with 1 column for label in {0, 1}
            pos_label (str, optional): positive class labels Defaults to 'TCR3d_pos'.
            neg_label (str, optional): negative class labels Defaults to 'TCRmodel2_neg'.
        """
        if type(df) == pd.DataFrame:
            self.original_data = df
        else:
            self.original_data = pd.read_csv(path)
        label_map = {0.0 : neg_label, 1.0 : pos_label}
        self.original_data['label'] = self.original_data['label'].map(label_map)
        self.feature_data = self.original_data.drop(columns=['label'], inplace=False)
        self.n_components = len(self.feature_data.columns)
        base_directory = 'Data_Analysis_png'
        self.subdirectory = str(path.split('/')[name_index].split('.')[0])
        self.path = os.path.join(base_directory, self.subdirectory)
        self.pos_label = pos_label
        self.neg_label = neg_label
        os.makedirs(self.path, exist_ok=True)

    def get_pca(self):
        # save loadings
        pca = PCA(n_components = self.n_components)
        X_pca = pca.fit_transform(self.feature_data.values)
        p_comp_matrix = pca.components_ ** 2
        principal_df = pd.DataFrame(data = p_comp_matrix, columns=self.feature_data.columns)

        fig1 = px.imshow(principal_df,
                         text_auto=False,
                         labels = dict(x = 'Feature', y = 'Principal Component'),
                         x = principal_df.columns,
                         y = principal_df.index,
                         title = f'Principal Component Loadings dataset {self.subdirectory}',
                         width=800, height=800)
        file_path1 = os.path.join(self.path, f'correlation_matrix.png')
        fig1.write_image(file_path1)

        # save first pca projection
        data = deepcopy(self.original_data)
        data['PCA1'] = X_pca[:, 0]
        data['PCA2'] = X_pca[:, 1]
        data['label'] = data['label'].astype(str)
        fig2 = px.scatter(data,
                          x = 'PCA1',
                          y = 'PCA2',
                          color = 'label',
                          color_discrete_sequence=['red', 'blue'],
                          title = f'PCA1 vs PCA2 on file {self.subdirectory}',
                          labels = {'PCA1':'PCA1', 'PCA2':'PCA2'},
                          width=800, height=800)
        file_path2 = os.path.join(self.path, f'PCA1_PCA2_scatter.png')
        fig2.write_image(file_path2)

    def pearson_correlation_matrix(self):
        corr_matrix = self.feature_data.corr()
        fig = px.imshow(corr_matrix,
                        text_auto=False,
                        labels = dict(x = 'Feature', y = 'Feature', color = 'Correlation'),
                        x = corr_matrix.columns,
                        y = corr_matrix.columns,
                        title=f"Correlation Matrix",
                        width=800, height=800)
        fig.update_layout(
        xaxis=dict(
            side="top"  
        ))
        file_path = os.path.join(self.path, f'correlation_matrix.png')
        fig.write_image(file_path)

    def distributions(self):
        color_map = {self.neg_label : 'red', self.pos_label : 'blue'}
        for feature in self.feature_data.columns:
            fig = make_subplots(rows = 1, cols = 2, subplot_titles=('Violin Plot', 'Histogram'))
            for label in self.original_data['label'].unique():
                fig.add_trace(
                    go.Violin(
                        x=self.original_data[self.original_data['label'] == label][feature],
                        name=label,
                        box_visible=True,
                        meanline_visible=True,
                        showlegend=True,
                        marker_color=color_map[label]
                    ),
                    row=1, col=1
                )
                fig.add_trace(
                    go.Histogram(
                        x=self.original_data[self.original_data['label'] == label][feature],
                        histnorm='density',
                        name=label,
                        marker_color=color_map[label],
                        showlegend=False
                    ),
                    row=1, col=2
                )
            fig.update_layout(title_text=f'Distribution of {feature}')
            file_path = os.path.join(self.path, f'{feature}_distribution.png')
            fig.write_image(file_path)






