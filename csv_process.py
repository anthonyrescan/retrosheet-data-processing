import pandas as pd
import os

#index_cols = ['GAME_ID','visitor_LINEUP1_BAT_ID']
#home_pivot_col1 = ['HOME_LINEUP1_FLD_CD']
#home_pivot_col2 = ['HOME_LINEUP2_BAT_ID','HOME_LINEUP2_FLD_CD']
#home_pivot_col3 = ['HOME_LINEUP3_BAT_ID','HOME_LINEUP3_FLD_CD']
#home_pivot_col4 = ['HOME_LINEUP4_BAT_ID','HOME_LINEUP4_FLD_CD']
#home_pivot_col5 = ['HOME_LINEUP5_BAT_ID','HOME_LINEUP5_FLD_CD']
#home_pivot_col6 = ['HOME_LINEUP6_BAT_ID','HOME_LINEUP6_FLD_CD']
#home_pivot_col7 = ['HOME_LINEUP7_BAT_ID','HOME_LINEUP7_FLD_CD']
#home_pivot_col8 = ['HOME_LINEUP8_BAT_ID','HOME_LINEUP8_FLD_CD']
#home_pivot_col9 = ['HOME_LINEUP9_BAT_ID','HOME_LINEUP9_FLD_CD']
#visitor_pivot_col1 = ['VISITOR_LINEUP1_BAT_ID','VISITOR_LINEUP1_FLD_CD']
#visitor_pivot_col2 = ['VISITOR_LINEUP2_BAT_ID','VISITOR_LINEUP2_FLD_CD']
#visitor_pivot_col3 = ['VISITOR_LINEUP3_BAT_ID','VISITOR_LINEUP3_FLD_CD']
#visitor_pivot_col4 = ['VISITOR_LINEUP4_BAT_ID','VISITOR_LINEUP4_FLD_CD']
#visitor_pivot_col5 = ['VISITOR_LINEUP5_BAT_ID','VISITOR_LINEUP5_FLD_CD']
#visitor_pivot_col6 = ['VISITOR_LINEUP6_BAT_ID','VISITOR_LINEUP6_FLD_CD']
#visitor_pivot_col7 = ['VISITOR_LINEUP7_BAT_ID','VISITOR_LINEUP7_FLD_CD']
#visitor_pivot_col8 = ['VISITOR_LINEUP8_BAT_ID','VISITOR_LINEUP8_FLD_CD']
#visitor_pivot_col9 = ['VISITOR_LINEUP9_BAT_ID','VISITOR_LINEUP9_FLD_CD']
#
#directory = os.path.dirname(__file__)
#ALCS_home = directory+'/2020ALCS_home_lineup.csv'
#ALCS_visit = directory+'/2020ALCS_visitor_lineup.csv'
#ALCS_home_df = pd.read_csv(ALCS_home)
#ALCS_home_df_1 = ALCS_home_df[["GAME_ID","HOME_LINEUP1_BAT_ID","HOME_LINEUP1_FLD_CD"]]
#ALCS_home_df_1 = ALCS_home_df[["GAME_ID","HOME_LINEUP1_BAT_ID","HOME_LINEUP1_FLD_CD"]]
#ALCS_home_df_1 = ALCS_home_df[["GAME_ID","HOME_LINEUP1_BAT_ID","HOME_LINEUP1_FLD_CD"]]
#ALCS_home_df_1 = ALCS_home_df[["GAME_ID","HOME_LINEUP1_BAT_ID","HOME_LINEUP1_FLD_CD"]]
#ALCS_home_df_1 = ALCS_home_df[["GAME_ID","HOME_LINEUP1_BAT_ID","HOME_LINEUP1_FLD_CD"]]
#ALCS_home_df_1 = ALCS_home_df[["GAME_ID","HOME_LINEUP1_BAT_ID","HOME_LINEUP1_FLD_CD"]]
#ALCS_home_df_1 = ALCS_home_df[["GAME_ID","HOME_LINEUP1_BAT_ID","HOME_LINEUP1_FLD_CD"]]
#ALCS_home_df_1 = ALCS_home_df[["GAME_ID","HOME_LINEUP1_BAT_ID","HOME_LINEUP1_FLD_CD"]]
#print(ALCS_home_df.head())
#ALCS_home_melt = pd.melt(ALCS_home_df_1,id_vars = index_cols)
#ALCS_home_melt.drop('variable',1,inplace=True)
#print(ALCS_home_melt)
#ALCS_home_melt = ALCS_home_melt.rename({'gameID' : 'gameID', 'HOME_LINEUP1_BAT_ID' : 'playerid', 'value' : 'field_pos'},axis=1)
#ALCS_home_melt['hometeam'] = True
#ALCS_home_melt['bat_order'] = 1
#
#print(ALCS_home_melt)

directory = os.path.dirname(__file__)

def process_home_lineups():
    file_count = []
    for filename in os.listdir(directory):
        if filename.endswith("home_lineup.csv") or filename.endswith("visitor_lineup.csv"):
            file_count.append(filename)
        else:
            continue
    if len(file_count) > 1:
        lineupfiles = []
        for filename in os.listdir(directory):
            if filename.endswith("home_lineup.csv") or filename.endswith("visitor_lineup.csv"): #need to do this in pairs so it merges the right files
                lineupfiles.append(filename)
            else:
                continue
    home_file = pd.read_csv(lineupfiles[0])
    index_cols1 = ['GAME_ID','HOME_LINEUP1_BAT_ID']
    home_pivot_col1 = ['HOME_LINEUP1_FLD_CD']
    index_cols2 = ['GAME_ID','HOME_LINEUP2_BAT_ID']
    home_pivot_col2 = ['HOME_LINEUP2_FLD_CD']
    index_cols3 = ['GAME_ID','HOME_LINEUP3_BAT_ID']
    home_pivot_col3 = ['HOME_LINEUP3_FLD_CD']
    index_cols4 = ['GAME_ID','HOME_LINEUP4_BAT_ID']
    home_pivot_col4 = ['HOME_LINEUP4_FLD_CD']
    index_cols5 = ['GAME_ID','HOME_LINEUP5_BAT_ID']
    home_pivot_col5 = ['HOME_LINEUP5_FLD_CD']
    index_cols6 = ['GAME_ID','HOME_LINEUP6_BAT_ID']
    home_pivot_col6 = ['HOME_LINEUP6_FLD_CD']
    index_cols7 = ['GAME_ID','HOME_LINEUP7_BAT_ID']
    home_pivot_col7 = ['HOME_LINEUP7_FLD_CD']
    index_cols8 = ['GAME_ID','HOME_LINEUP8_BAT_ID']
    home_pivot_col8 = ['HOME_LINEUP8_FLD_CD']
    index_cols9 = ['GAME_ID','HOME_LINEUP9_BAT_ID']
    home_pivot_col9 = ['HOME_LINEUP9_FLD_CD']
    home_df_1 = home_file[["GAME_ID","HOME_LINEUP1_BAT_ID","HOME_LINEUP1_FLD_CD"]]
    home_df_2 = home_file[["GAME_ID","HOME_LINEUP2_BAT_ID","HOME_LINEUP2_FLD_CD"]]
    home_df_3 = home_file[["GAME_ID","HOME_LINEUP3_BAT_ID","HOME_LINEUP3_FLD_CD"]]
    home_df_4 = home_file[["GAME_ID","HOME_LINEUP4_BAT_ID","HOME_LINEUP4_FLD_CD"]]
    home_df_5 = home_file[["GAME_ID","HOME_LINEUP5_BAT_ID","HOME_LINEUP5_FLD_CD"]]
    home_df_6 = home_file[["GAME_ID","HOME_LINEUP6_BAT_ID","HOME_LINEUP6_FLD_CD"]]
    home_df_7 = home_file[["GAME_ID","HOME_LINEUP7_BAT_ID","HOME_LINEUP7_FLD_CD"]]
    home_df_8 = home_file[["GAME_ID","HOME_LINEUP8_BAT_ID","HOME_LINEUP8_FLD_CD"]]
    home_df_9 = home_file[["GAME_ID","HOME_LINEUP9_BAT_ID","HOME_LINEUP9_FLD_CD"]]
    home_melt1 = pd.melt(home_df_1,id_vars = index_cols1)
    home_melt2 = pd.melt(home_df_2,id_vars = index_cols2)
    home_melt3 = pd.melt(home_df_3,id_vars = index_cols3)
    home_melt4 = pd.melt(home_df_4,id_vars = index_cols4)
    home_melt5 = pd.melt(home_df_5,id_vars = index_cols5)
    home_melt6 = pd.melt(home_df_6,id_vars = index_cols6)
    home_melt7 = pd.melt(home_df_7,id_vars = index_cols7)
    home_melt8 = pd.melt(home_df_8,id_vars = index_cols8)
    home_melt9 = pd.melt(home_df_9,id_vars = index_cols9)
    home_melt1.drop('variable',1,inplace=True)
    home_melt2.drop('variable',1,inplace=True)
    home_melt3.drop('variable',1,inplace=True)
    home_melt4.drop('variable',1,inplace=True)
    home_melt5.drop('variable',1,inplace=True)
    home_melt6.drop('variable',1,inplace=True)
    home_melt7.drop('variable',1,inplace=True)
    home_melt8.drop('variable',1,inplace=True)
    home_melt9.drop('variable',1,inplace=True)
    home_melt1 = home_melt1.rename({'gameID' : 'gameID', 'HOME_LINEUP1_BAT_ID' : 'playerid', 'value' : 'field_pos'},axis=1)
    home_melt2 = home_melt2.rename({'gameID' : 'gameID', 'HOME_LINEUP2_BAT_ID' : 'playerid', 'value' : 'field_pos'},axis=1)
    home_melt3 = home_melt3.rename({'gameID' : 'gameID', 'HOME_LINEUP3_BAT_ID' : 'playerid', 'value' : 'field_pos'},axis=1)
    home_melt4 = home_melt4.rename({'gameID' : 'gameID', 'HOME_LINEUP4_BAT_ID' : 'playerid', 'value' : 'field_pos'},axis=1)
    home_melt5 = home_melt5.rename({'gameID' : 'gameID', 'HOME_LINEUP5_BAT_ID' : 'playerid', 'value' : 'field_pos'},axis=1)
    home_melt6 = home_melt6.rename({'gameID' : 'gameID', 'HOME_LINEUP6_BAT_ID' : 'playerid', 'value' : 'field_pos'},axis=1)
    home_melt7 = home_melt7.rename({'gameID' : 'gameID', 'HOME_LINEUP7_BAT_ID' : 'playerid', 'value' : 'field_pos'},axis=1)
    home_melt8 = home_melt8.rename({'gameID' : 'gameID', 'HOME_LINEUP8_BAT_ID' : 'playerid', 'value' : 'field_pos'},axis=1)
    home_melt9 = home_melt9.rename({'gameID' : 'gameID', 'HOME_LINEUP9_BAT_ID' : 'playerid', 'value' : 'field_pos'},axis=1)
    home_melt1['bat_order'] = 1
    home_melt2['bat_order'] = 2
    home_melt3['bat_order'] = 3
    home_melt4['bat_order'] = 4
    home_melt5['bat_order'] = 5
    home_melt6['bat_order'] = 6
    home_melt7['bat_order'] = 7
    home_melt8['bat_order'] = 8
    home_melt9['bat_order'] = 9
    home_concat = pd.concat([home_melt1,home_melt2,home_melt3,home_melt4,home_melt5,home_melt6,home_melt7,home_melt8,home_melt9])
    home_concat['hometeam'] = True
    print(home_concat.head())
    output_home_lineup = (home_file[0:-15]+'home_lineup.csv')
    print(output_home_lineup)

def process_visitor_lineups():
    file_count = []
    for filename in os.listdir(directory):
        if filename.endswith("visitor_lineup.csv"):
            file_count.append(filename)
        else:
            continue
    if len(file_count) > 1:
        lineupfiles = []
        for filename in os.listdir(directory):
            if filename.endswith("visitor_lineup.csv"):
                lineupfiles.append(filename)
            else:
                continue
    visitor_file = pd.read_csv(lineupfiles[0])
    index_cols1 = ['GAME_ID','visitor_LINEUP1_BAT_ID']
    visitor_pivot_col1 = ['visitor_LINEUP1_FLD_CD']
    index_cols2 = ['GAME_ID','visitor_LINEUP2_BAT_ID']
    visitor_pivot_col2 = ['visitor_LINEUP2_FLD_CD']
    index_cols3 = ['GAME_ID','visitor_LINEUP3_BAT_ID']
    visitor_pivot_col3 = ['visitor_LINEUP3_FLD_CD']
    index_cols4 = ['GAME_ID','visitor_LINEUP4_BAT_ID']
    visitor_pivot_col4 = ['visitor_LINEUP4_FLD_CD']
    index_cols5 = ['GAME_ID','visitor_LINEUP5_BAT_ID']
    visitor_pivot_col5 = ['visitor_LINEUP5_FLD_CD']
    index_cols6 = ['GAME_ID','visitor_LINEUP6_BAT_ID']
    visitor_pivot_col6 = ['visitor_LINEUP6_FLD_CD']
    index_cols7 = ['GAME_ID','visitor_LINEUP7_BAT_ID']
    visitor_pivot_col7 = ['visitor_LINEUP7_FLD_CD']
    index_cols8 = ['GAME_ID','visitor_LINEUP8_BAT_ID']
    visitor_pivot_col8 = ['visitor_LINEUP8_FLD_CD']
    index_cols9 = ['GAME_ID','visitor_LINEUP9_BAT_ID']
    visitor_pivot_col9 = ['visitor_LINEUP9_FLD_CD']
    visitor_df_1 = visitor_file[["GAME_ID","visitor_LINEUP1_BAT_ID","visitor_LINEUP1_FLD_CD"]]
    visitor_df_2 = visitor_file[["GAME_ID","visitor_LINEUP2_BAT_ID","visitor_LINEUP2_FLD_CD"]]
    visitor_df_3 = visitor_file[["GAME_ID","visitor_LINEUP3_BAT_ID","visitor_LINEUP3_FLD_CD"]]
    visitor_df_4 = visitor_file[["GAME_ID","visitor_LINEUP4_BAT_ID","visitor_LINEUP4_FLD_CD"]]
    visitor_df_5 = visitor_file[["GAME_ID","visitor_LINEUP5_BAT_ID","visitor_LINEUP5_FLD_CD"]]
    visitor_df_6 = visitor_file[["GAME_ID","visitor_LINEUP6_BAT_ID","visitor_LINEUP6_FLD_CD"]]
    visitor_df_7 = visitor_file[["GAME_ID","visitor_LINEUP7_BAT_ID","visitor_LINEUP7_FLD_CD"]]
    visitor_df_8 = visitor_file[["GAME_ID","visitor_LINEUP8_BAT_ID","visitor_LINEUP8_FLD_CD"]]
    visitor_df_9 = visitor_file[["GAME_ID","visitor_LINEUP9_BAT_ID","visitor_LINEUP9_FLD_CD"]]
    visitor_melt1 = pd.melt(visitor_pivot_col1,id_vars = index_cols1)
    visitor_melt2 = pd.melt(visitor_pivot_col2,id_vars = index_cols2)
    visitor_melt3 = pd.melt(visitor_pivot_col3,id_vars = index_cols3)
    visitor_melt4 = pd.melt(visitor_pivot_col4,id_vars = index_cols4)
    visitor_melt5 = pd.melt(visitor_pivot_col5,id_vars = index_cols5)
    visitor_melt6 = pd.melt(visitor_pivot_col6,id_vars = index_cols6)
    visitor_melt7 = pd.melt(visitor_pivot_col7,id_vars = index_cols7)
    visitor_melt8 = pd.melt(visitor_pivot_col8,id_vars = index_cols8)
    visitor_melt9 = pd.melt(visitor_pivot_col9,id_vars = index_cols9)
    visitor_melt1.drop('variable',1,inplace=True)
    visitor_melt2.drop('variable',1,inplace=True)
    visitor_melt3.drop('variable',1,inplace=True)
    visitor_melt4.drop('variable',1,inplace=True)
    visitor_melt5.drop('variable',1,inplace=True)
    visitor_melt6.drop('variable',1,inplace=True)
    visitor_melt7.drop('variable',1,inplace=True)
    visitor_melt8.drop('variable',1,inplace=True)
    visitor_melt9.drop('variable',1,inplace=True)
    visitor_melt1 = visitor_melt1.rename({'gameID' : 'gameID', 'visitor_LINEUP1_BAT_ID' : 'playerid', 'value' : 'field_pos'},axis=1)
    visitor_melt2 = visitor_melt2.rename({'gameID' : 'gameID', 'visitor_LINEUP2_BAT_ID' : 'playerid', 'value' : 'field_pos'},axis=1)
    visitor_melt3 = visitor_melt3.rename({'gameID' : 'gameID', 'visitor_LINEUP3_BAT_ID' : 'playerid', 'value' : 'field_pos'},axis=1)
    visitor_melt4 = visitor_melt4.rename({'gameID' : 'gameID', 'visitor_LINEUP4_BAT_ID' : 'playerid', 'value' : 'field_pos'},axis=1)
    visitor_melt5 = visitor_melt5.rename({'gameID' : 'gameID', 'visitor_LINEUP5_BAT_ID' : 'playerid', 'value' : 'field_pos'},axis=1)
    visitor_melt6 = visitor_melt6.rename({'gameID' : 'gameID', 'visitor_LINEUP6_BAT_ID' : 'playerid', 'value' : 'field_pos'},axis=1)
    visitor_melt7 = visitor_melt7.rename({'gameID' : 'gameID', 'visitor_LINEUP7_BAT_ID' : 'playerid', 'value' : 'field_pos'},axis=1)
    visitor_melt8 = visitor_melt8.rename({'gameID' : 'gameID', 'visitor_LINEUP8_BAT_ID' : 'playerid', 'value' : 'field_pos'},axis=1)
    visitor_melt9 = visitor_melt9.rename({'gameID' : 'gameID', 'visitor_LINEUP9_BAT_ID' : 'playerid', 'value' : 'field_pos'},axis=1)
    visitor_melt1['bat_order'] = 1
    visitor_melt2['bat_order'] = 2
    visitor_melt3['bat_order'] = 3
    visitor_melt4['bat_order'] = 4
    visitor_melt5['bat_order'] = 5
    visitor_melt6['bat_order'] = 6
    visitor_melt7['bat_order'] = 7
    visitor_melt8['bat_order'] = 8
    visitor_melt9['bat_order'] = 9
    visitor_concat = pd.concat()
    visitor_concat['hometeam'] = True
    output_visitor_lineup = (visitor_concat[0:-15]+'visitor_lineup.csv')
    print(output_visitor_lineup)
    output_file_lineup = (visitor_file[0:-15]+'visitor_lineup.csv')
    print(output_file_lineup)

print(process_home_lineups())