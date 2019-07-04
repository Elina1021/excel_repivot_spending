
# coding: utf-8

# In[1]:


import pandas as pd
import os


# In[2]:


def read_excel(filename, sheet_name: str = 'data'):
    '''读取原始数据, 返回dataframe
    '''
    df = pd.read_excel(filename, sheet_name=sheet_name)
    return df


# In[3]:


def get_drop_cols(months):
    '''获取要删除的列
    months: 要保留的列
    '''
    fixed_drop_col = '折算花费（万元）'  # 固定删除列
    month_lst = list(range(1, 13))  # 1-12月
    for month in months:
        month_lst.remove(month)  # 在要删除的列中排除所需的列
    drop_cols = [str(i) + '月' for i in month_lst]  # 要删除的列名列表
    drop_cols.append(fixed_drop_col)
    return drop_cols


# In[4]:


def main(filename):
    if not filename:
        raise AssertionError('filename must be input!')
    output_filename = 'currentdata.txt'
    
    months = [4]
    
    year = 2019
    BRANDS = ['奔驰','凯迪拉克','捷豹','奥迪','宝马','雷克萨斯','阿尔法罗密欧',
             '路虎','林肯','沃尔沃','保时捷','英菲尼迪','DS','讴歌','Smart','MINI']# AR所需品牌 
    criteria_rows = {'年份':[year],
                     '品牌':BRANDS}
    
    INDEX_COLUMNS = ['数据源','车型','品牌','汽车厂商','类型','媒体大类','媒体中类','媒体名称',
                 '折算系数','省份','城市','UD-显示屏','UD-视频/非视频','FCA_SUVSeg',
                 'FCA_Region','FCA_KeyCom','FCA_Tier','Remark','年份']

    
    df = read_excel(filename,sheet_name='data')
    # 删除列
    drop_cols = get_drop_cols(months)
    df = df.drop(drop_cols,axis=1)
    # 筛选行
    for k,v in criteria_rows.items():
        df = df[df[k].isin(v)]
    # 数据旋转
    df = df.set_index(INDEX_COLUMNS).stack().reset_index()
    # 重命名列
        ## 如何自动判断
    col_month_name = '月份'
    col_data_name = '折算花费（万元）'
    columns_rename_dict = {'level_19':col_month_name,0:col_data_name} 
    df = df.rename(columns_rename_dict,axis=1)
    # 值调整
    df[col_month_name] = df[col_month_name].str.replace(col_month_name[0],'').astype(int)
    # 输出到csv
    df.to_csv(output_filename,sep='\t',header=True, index=False)
    
    try:
        os.startfile(output_filename)
    except Exception as e:
        print(e)
        raise
    
    print(f'please find the datafile {output_filename},thanks')


# In[5]:


if __name__ == '__main__':
    filename = 'data.xlsx'
    main(filename)

