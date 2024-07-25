from modelApi import modelApi
import json


def extract_query_and_chart_info(text):
  json_string = text
  data = json.loads(json_string)

  chart_type = data['chart']
  x_axis = data['x-axis']
  y_axis = data['y-axis']

  return chart_type, x_axis, y_axis


def recommend_chart(response):

    db_chain,chain,meta = modelApi()
    # chart_prompt = f"""For the sql_query: {response} ,
    # suggest the type of chart and the columns that can be used for x and y axes.
    # *Make sure that your response is in JSON form,Reply with only the answer in JSON form include no other commentary.
    # You can use the below example for reference -
    #
    # Chart: bar,x-axis: column1,y-axis: column2
    #
    # """

    chart_prompt = f"""For the sql_query: {response},
suggest the type of chart and the columns that can be used for x and y axes.
*Make sure that your response is in JSON form. Reply with only the answer in JSON form. Include no other commentary.
Your JSON response should follow this template:

{{
    "chart": "chart_type",
    "x-axis": "column_name",
    "y-axis": "column_name"
}}

Example:
{{
    "chart": "bar",
    "x-axis": "column1",
    "y-axis": "column2"
}}
"""
    try:
        result = db_chain.run(chart_prompt)
        print(f'Result from recommended chart -> {result}')

        chart, x_column, y_columns = extract_query_and_chart_info(result)
        return chart, x_column, y_columns

    except Exception as e:
        print(f"Error occurred: {e}")
        return None, None, None