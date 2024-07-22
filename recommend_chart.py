from modelApi import modelApi
import json


def extract_query_and_chart_info(text):
  json_string = text
  data = json.loads(json_string)

  print()

  chart_type = data['Chart']
  x_axis = data['x-axis']
  y_axis = data['y-axis']

  return chart_type, x_axis, y_axis


def recommend_chart(response):

    db_chain,chain,meta = modelApi()
    chart_prompt = f"""For the sql_query: {response} ,
    suggest the type of chart and the columns that can be used for x and y axes.
    *Make sure that your response is in JSON form,Reply with only the answer in JSON form include no other commentary.
    You can use the below example for reference -

    Chart: bar,x-axis: column1,y-axis: column2

    """
    result = db_chain.run(chart_prompt)

    chart,x_column,y_columns = extract_query_and_chart_info(result)

    return chart,x_column,y_columns