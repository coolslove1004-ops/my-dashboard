{\rtf1\ansi\ansicpg949\cocoartf2869
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww21560\viewh12320\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf0 \expnd0\expndtw0\kerning0
import streamlit as st\
import pandas as pd\
import plotly.express as px\
\
# 1. \uc0\u54168 \u51060 \u51648  \u44592 \u48376  \u49444 \u51221 \
st.set_page_config(page_title="\uc0\u49888 \u51228 \u54408  \u44060 \u48156  \u51652 \u52377  \u45824 \u49884 \u48372 \u46300 ", layout="wide")\
st.title("\uc0\u55357 \u56522  [\u47560 \u52992 \u54021 \u48512 ] \u49888 \u51228 \u54408  \u44060 \u48156  \u51652 \u52377  \u54788 \u54889  \u45824 \u49884 \u48372 \u46300 ")\
st.markdown("\uc0\u47588 \u51452  \u52712 \u54633 \u46104 \u45716  \u49888 \u51228 \u54408  \u44060 \u48156  \u54788 \u54889  \u54028 \u51068 \u51012  \u50629 \u47196 \u46300 \u54616 \u47732  \u49892 \u49884 \u44036 \u51004 \u47196  \u50836 \u50557  \u45936 \u51060 \u53552 \u50752  \u47532 \u49828 \u53356 \u47484  \u49884 \u44033 \u54868 \u54633 \u45768 \u45796 .")\
\
# 2. \uc0\u54028 \u51068  \u50629 \u47196 \u45908 \
uploaded_file = st.file_uploader("\uc0\u50641 \u49472  \u46608 \u45716  CSV \u54028 \u51068 \u51012  \u50629 \u47196 \u46300 \u54616 \u49464 \u50836 .", type=["csv", "xlsx"])\
\
if uploaded_file is not None:\
    try:\
        # [\uc0\u49688 \u51221  \u54252 \u51064 \u53944 ] \u54028 \u51068  \u54805 \u49885 \u50640  \u44288 \u44228 \u50630 \u51060  \u50896 \u48376 \u51032  \u49345 \u45800  \u53440 \u51060 \u53952 /\u48712 \u54665 \u51012  \u47924 \u49884 \u54616 \u44256  \
        # 'No.'\uc0\u44032  \u54252 \u54632 \u46108  \u51652 \u51676  \u54756 \u45908  \u54665 \u51012  \u51088 \u46041 \u51004 \u47196  \u52286 \u50500 \u49436  \u51069 \u50612 \u50724 \u45716  \u47196 \u51649  \u51201 \u50857 \
        if uploaded_file.name.endswith('.csv'):\
            # CSV \uc0\u54028 \u51068 \u51064  \u44221 \u50864  \u50864 \u49440  \u47928 \u51088 \u50676 \u47196  \u51069 \u51008  \u46244  \u54756 \u45908  \u50948 \u52824  \u54028 \u50501 \
            lines = uploaded_file.getvalue().decode('utf-8').split('\\n')\
            skip_idx = 0\
            for i, line in enumerate(lines):\
                if 'No.' in line and '\uc0\u51228 \u54408 \u47749 ' in line:\
                    skip_idx = i\
                    break\
            uploaded_file.seek(0)\
            raw_df = pd.read_csv(uploaded_file, skiprows=skip_idx)\
        else:\
            # Excel \uc0\u54028 \u51068 \u51064  \u44221 \u50864 \
            excel_file = pd.ExcelFile(uploaded_file)\
            sheet_df = excel_file.parse(excel_file.sheet_names[0], header=None)\
            skip_idx = 0\
            for idx, row in sheet_df.iterrows():\
                if 'No.' in row.values and '\uc0\u51228 \u54408 \u47749 ' in row.values:\
                    skip_idx = idx\
                    break\
            raw_df = excel_file.parse(excel_file.sheet_names[0], skiprows=skip_idx)\
        \
        # \uc0\u54596 \u50836 \u54620  \u44277 \u53685  14\u44060  \u52972 \u47100 \u47564  \u49836 \u46972 \u51060 \u49905  \u48143  \u51060 \u47492  \u53685 \u51068 \
        raw_df = raw_df.iloc[:, :14]\
        raw_df.columns = [\
            'No.', '\uc0\u44396 \u48516 ', '\u51228 \u54408 \u47749 ', '\u45812 \u45817 \u51088 ', '\u51228 \u54408  \u44396 \u48516 ', '\u52636 \u49884  \u47785 \u54364 ', \
            '\uc0\u48176 \u54633 \u48708 ', '\u46356 \u51088 \u51064 ', '\u49884 \u49373 \u49328 ', '\u54252 \u51109 \u48156 \u51452 ', '\u50696 \u49345  \u52636 \u49884 ', '\u49464 \u48512  \u45236 \u50857 ', '\u49373 \u49328 \u52376 ', '\u51452 \u50836 \u52292 \u45328 '\
        ]\
        \
        # \uc0\u45936 \u51060 \u53552  \u53364 \u47532 \u45789 : 'No.'\u50676 \u51060  \u48708 \u50612 \u51080 \u44144 \u45208  \u49707 \u51088 \u44032  \u50500 \u45772  \u54665 (\u50696 : \u54616 \u45800  \u44277 \u48177 , \u51473 \u44036  \u53440 \u51060 \u53952 ) \u51228 \u44144 \
        df = raw_df[pd.to_numeric(raw_df['No.'], errors='coerce').notna()].copy()\
        df['No.'] = df['No.'].astype(int)\
        \
        # 3. \uc0\u45936 \u51060 \u53552  \u49345 \u53468  \u48516 \u47448  \u47196 \u51649 \
        def determine_status(row):\
            expected = str(row['\uc0\u50696 \u49345  \u52636 \u49884 ']).strip()\
            target = str(row['\uc0\u52636 \u49884  \u47785 \u54364 ']).strip()\
            \
            if '\uc0\u52636 \u49884 \u50756 \u47308 ' in expected:\
                return '\uc0\u52636 \u49884  \u50756 \u47308 '\
            elif expected == '\uc0\u48120 \u51221 ' or target == '\u48120 \u51221 ' or expected == 'nan':\
                return '\uc0\u48120 \u51221 '\
            elif target != expected:\
                return '\uc0\u51648 \u50672 /\u47532 \u49828 \u53356 '\
            else:\
                return '\uc0\u51221 \u49345  \u51652 \u54665 '\
            \
        df['\uc0\u51652 \u54665 \u49345 \u53468 '] = df.apply(determine_status, axis=1)\
\
        # 4. \uc0\u49345 \u45800  KPI \u49828 \u53076 \u50612 \u48372 \u46300  \u48176 \u52824 \
        total_tasks = len(df)\
        completed = len(df[df['\uc0\u51652 \u54665 \u49345 \u53468 '] == '\u52636 \u49884  \u50756 \u47308 '])\
        in_progress = len(df[df['\uc0\u51652 \u54665 \u49345 \u53468 '] == '\u51221 \u49345  \u51652 \u54665 '])\
        delayed = len(df[df['\uc0\u51652 \u54665 \u49345 \u53468 '] == '\u51648 \u50672 /\u47532 \u49828 \u53356 '])\
        \
        comp_rate = (completed / total_tasks * 100) if total_tasks > 0 else 0\
\
        kpi1, kpi2, kpi3, kpi4 = st.columns(4)\
        kpi1.metric("\uc0\u52509  \u44284 \u51228  \u49688 ", f"\{total_tasks\} \u44148 ")\
        kpi2.metric("\uc0\u52636 \u49884  \u50756 \u47308 ", f"\{completed\} \u44148 ", f"\u45804 \u49457 \u47456  \{comp_rate:.1f\}%")\
        kpi3.metric("\uc0\u51221 \u49345  \u51652 \u54665 ", f"\{in_progress\} \u44148 ")\
        kpi4.metric("\uc0\u51648 \u50672  / \u47532 \u49828 \u53356  \u55357 \u57000 ", f"\{delayed\} \u44148 ", delta=f"-\{delayed\}\u44148  \u44288 \u47532  \u54596 \u50836 ", delta_color="inverse")\
\
        st.markdown("---")\
\
        # 5. \uc0\u52264 \u53944  \u49465 \u49496  (\u51340 \u50864  2\u48516 \u54624 )\
        col1, col2 = st.columns(2)\
\
        with col1:\
            st.subheader("\uc0\u55356 \u57314  \u48512 \u49436 \u48324  \u44284 \u51228  \u54788 \u54889 ")\
            dept_df = df.groupby(['\uc0\u44396 \u48516 ', '\u51652 \u54665 \u49345 \u53468 ']).size().reset_index(name='\u44148 \u49688 ')\
            fig_dept = px.bar(\
                dept_df, x='\uc0\u44396 \u48516 ', y='\u44148 \u49688 ', color='\u51652 \u54665 \u49345 \u53468 ', barmode='group',\
                color_discrete_map=\{'\uc0\u52636 \u49884  \u50756 \u47308 ': '#2ecc71', '\u51221 \u49345  \u51652 \u54665 ': '#3498db', '\u51648 \u50672 /\u47532 \u49828 \u53356 ': '#e74c3c', '\u48120 \u51221 ': '#95a5a6'\},\
                text_auto=True\
            )\
            fig_dept.update_layout(xaxis_title=None, yaxis_title="\uc0\u44284 \u51228  \u49688 ")\
            st.plotly_chart(fig_dept, use_container_width=True)\
\
        with col2:\
            st.subheader("\uc0\u55356 \u57173  \u44284 \u51228  \u50976 \u54805 \u48324  \u48708 \u51473  (\u49888 \u51228 \u54408  vs \u47532 \u45684 \u50620 )")\
            type_df = df.groupby('\uc0\u51228 \u54408  \u44396 \u48516 ').size().reset_index(name='\u44148 \u49688 ')\
            fig_pie = px.pie(\
                type_df, values='\uc0\u44148 \u49688 ', names='\u51228 \u54408  \u44396 \u48516 ', hole=0.4,\
                color_discrete_sequence=px.colors.qualitative.Pastel\
            )\
            fig_pie.update_traces(textinfo='percent+value')\
            st.plotly_chart(fig_pie, use_container_width=True)\
\
        st.markdown("---")\
\
        # 6. \uc0\u54616 \u45800  \u47532 \u49828 \u53356  \u51665 \u51473  \u44288 \u47532  \u49465 \u49496 \
        st.subheader("\uc0\u55357 \u57000  \u51060 \u48264  \u51452  \u51665 \u51473  \u44288 \u47532  \u51648 \u50672  \u44284 \u51228  \u47532 \u49828 \u53944 ")\
        delay_df = df[df['\uc0\u51652 \u54665 \u49345 \u53468 '] == '\u51648 \u50672 /\u47532 \u49828 \u53356 '][['\u44396 \u48516 ', '\u51228 \u54408 \u47749 ', '\u45812 \u45817 \u51088 ', '\u52636 \u49884  \u47785 \u54364 ', '\u50696 \u49345  \u52636 \u49884 ', '\u49464 \u48512  \u45236 \u50857 ', '\u49373 \u49328 \u52376 ']]\
        \
        if len(delay_df) > 0:\
            st.dataframe(\
                delay_df, \
                column_config=\{"\uc0\u49464 \u48512  \u45236 \u50857 ": st.column_config.TextColumn("\u51648 \u50672  \u49324 \u50976  (\u49464 \u48512  \u45236 \u50857 )", width="large")\},\
                use_container_width=True,\
                hide_index=True\
            )\
        else:\
            st.success("\uc0\u54788 \u51116  \u51648 \u50672 \u46108  \u44284 \u51228 \u44032  \u50630 \u49845 \u45768 \u45796 ! \u47784 \u46160  \u51221 \u49345  \u51652 \u54665  \u51473 \u51077 \u45768 \u45796 .")\
\
        # 7. \uc0\u51204 \u52404  \u45936 \u51060 \u53552  \u51312 \u54924 \u50857  \u53580 \u51060 \u48660 \
        with st.expander("\uc0\u55357 \u56589  \u51204 \u52404  \u45936 \u51060 \u53552  \u47532 \u49828 \u53944  \u54869 \u51064 \u54616 \u44592 "):\
            st.dataframe(df.drop(columns=['\uc0\u51652 \u54665 \u49345 \u53468 ']), use_container_width=True, hide_index=True)\
\
    except Exception as e:\
        st.error(f"\uc0\u54028 \u51068 \u51012  \u51069 \u45716  \u51473  \u50724 \u47448 \u44032  \u48156 \u49373 \u54664 \u49845 \u45768 \u45796 . \u54028 \u51068  \u54805 \u49885 \u51012  \u54869 \u51064 \u54644  \u51452 \u49464 \u50836 . \u50724 \u47448  \u45236 \u50857 : \{e\}")}