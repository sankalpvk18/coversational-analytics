from charting import create_chart
from databaseApi import get_data
from modelApi import modelApi
from prompt import get_prompt
from recommend_chart import recommend_chart


def get_result(question):
    db_chain, chain, meta = modelApi()
    prompt = get_prompt(question, meta)
    response = chain.invoke({"question": prompt})
    chart, x_column, y_columns = recommend_chart(response)

    data = get_data(response)

    fig = None
    if len(data) > 1:
        fig = create_chart(data, chart, x_column, y_columns)

    return data, fig, response, chart, x_column, y_columns
