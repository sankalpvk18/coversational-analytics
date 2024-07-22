#new charting module
import plotly.express as px

def create_chart(df, chart_type, x_column, y_columns):
    """
    Create a chart using Plotly Express.

    Parameters:
        df (DataFrame): The DataFrame containing the data.
        chart_type (str): The type of chart to create (line, bar, pie, stacked bar).
        x_column (str): The column name for the x-axis.
        y_columns (list of str): The list of column names for the y-axis.

    Returns:
        fig: The Plotly figure object.
    """
    if chart_type == 'line':
        fig = px.line(df, x=x_column, y=y_columns, title=f'Line Chart: {x_column} vs {y_columns}')
    elif chart_type == 'bar':
        fig = px.bar(df, x=x_column, y=y_columns, title=f'Bar Chart: {x_column} vs {y_columns}')
    elif chart_type == 'pie':
        fig = px.pie(df, values=y_columns[0], names=x_column, title=f'Pie Chart: {x_column} vs {y_columns}')
    elif chart_type == 'stacked bar':
        fig = px.bar(df, x=x_column, y=y_columns, title=f'Stacked Bar Chart: {x_column} vs {y_columns}', barmode='stack')
    else:
        raise ValueError("Invalid chart type. Please choose one of 'line', 'bar', 'pie', or 'stacked bar'.")

    return fig