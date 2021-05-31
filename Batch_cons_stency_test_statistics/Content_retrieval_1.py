import pandas as pd


def excel_one_line_to_list():
    df = pd.read_excel("test2.xlsx", sheet_name = "Sheet1",
                       usecols=[0], names=None)  # 读取项目名称列,不要列名
    df_li = df.values.tolist()
    result = []
    for s_li in df_li:
        result.append(str(s_li[0]))
    return result
    


if __name__ == '__main__':
    courier_list = excel_one_line_to_list()
    print(courier_list)
