import plotly.express as px


class charts:

    @staticmethod
    def treatment_start_year_chart(data):
        column = 'Moed thilat tipul'
        year_counts = year_counts = data[data[column] != 0][column].value_counts().sort_index()
        fig = px.bar(x=year_counts.index, y=year_counts.values, labels={'x': 'Year', 'y': 'Count'})
        fig.update_layout(title=f"Frequency of Each Year in '{column}'", xaxis_title="Year", yaxis_title="Frequency")
        return fig

    @staticmethod
    def create_polluting_activity_chart(data):
        activity_counts = data['Peelut mezahemet'].value_counts()
        fig = px.pie(values=activity_counts.values, names=activity_counts.index,
                     title='Distribution of Polluting Activity')
        return fig

    @staticmethod
    def create_safety_buildings_chart(data):
        requirement_counts = data['Drisha lemigun mivnim'].value_counts()
        fig = px.pie(values=requirement_counts.values, names=requirement_counts.index,
                     title='Requirement for Safety Buildings')
        return fig

    @staticmethod
    def create_administrative_status_chart(data):
        status_counts = data['Matzav Minhali'].value_counts()
        fig = px.pie(values=status_counts.values, names=status_counts.index,
                     title='Distribution of Administrative Status')
        return fig
