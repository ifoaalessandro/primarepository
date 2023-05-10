import streamlit as st
import pandas as pd
import numpy as np
import matplotlib
import sklearn
import mlem
import io


def main():

    st.title("template")

    uploaded_file = st.file_uploader("Choose a file",type={"csv"})
    if uploaded_file is not None:
        ###### transformation #####################################
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)

        # st.write(df)
        df = df.drop(columns='Profit')
        st.dataframe(df)
        X = df.copy()

        new_model = mlem.api.load('model_.mlem')

        # x1 = st.slider("Inserire R&D Spend:", 1, 100000, 1)
        # x2 = st.slider("Inserire Administration:", 1, 100000, 1)
        # x3 = st.slider("Inserire Marketing Spend:", 1, 100000, 1)

        res = new_model.predict(X)
        
        st.title("Model predict")
        st.write(res.round(2))
        df['Prediction']=res
        st.dataframe(df)

        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            # Write each dataframe to a different worksheet.
            df.to_excel(writer, index=False)
            # Close the Pandas Excel writer and output the Excel file to the buffer
            writer.save()
            st.download_button(
                label="Download Excel Result",
                data=buffer,
                file_name="trasnformed_file.xlsx",
                mime="application/vnd.ms-excel")
    
    else:
        st.warning("File CSV is required")




if __name__ == "__main__":
    main()

 if st.button('Scarica Excel'):
        output = io.BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        input_df.to_excel(writer, index=False, sheet_name='Input')
        pd.DataFrame(prediction, columns=['Profitto previsto']).to_excel(writer, index=False, sheet_name='Output')
        writer.save()
        output.seek(0)
        st.download_button(label="Download", data=output, file_name='output.xlsx', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',)str