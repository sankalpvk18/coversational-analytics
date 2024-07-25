from charting import create_chart
from databaseApi import get_data
from modelApi import modelApi
from prompt import get_prompt
from recommend_chart import recommend_chart


def get_result(question):
    db_chain, chain, meta = modelApi()
    prompt = get_prompt(question, meta)
    response = chain.invoke({"question": prompt})
    print(f'Response -- {response}')
    chart, x_column, y_columns = recommend_chart(response)
    print(f'chart -- {chart}')
    print(f'x_column -- {x_column}')
    print(f'y_columns -- {y_columns}')
    data = get_data(response)

    fig = None
    if len(data) > 1:
        fig = create_chart(data, chart, x_column, y_columns)

    return data, fig, response, chart, x_column, y_columns
