import streamlit as st 
import pickle

st.set_page_config(page_title= "Telecom",
                   page_icon= '💻',
                   layout= "wide",)

text = 'Telecom Customer Churn'   
st.markdown(f"<h2 style='color: black; text-align: center;'>{text} </h2>", unsafe_allow_html=True)
st.write("<hr>", unsafe_allow_html=True)

st.subheader('Basic Details')
col1,col2,col3 = st.columns([1,1,1])

gender = col1.selectbox('Gender:',['male','female'],index=None, placeholder="Select Gender...")

SeniorCitizen_option = ({"Yes":1,"No":0 })
SeniorCitizen = col2.selectbox('Senior Citizen:',list(SeniorCitizen_option.keys()),index=None, placeholder="Select SeniorCitizen...")

partner_option = ({'Yes':1,'No':0})
Partner = col3.selectbox('Partner:',list(partner_option.keys()),index=None, placeholder="Select Partner...")

Dependents_option = ({'Yes':1,'No':0})
Dependents = col1.selectbox('Dependents',list(Dependents_option.keys()),index=None, placeholder="Select Partner...")

st.subheader("Services")
col4,col5,col6 = st.columns([1,1,1])

PhoneService_option = ({'Yes':1, 'No':0})
PhoneService = col4.selectbox('Phone Service', list(PhoneService_option.keys()),index=None, placeholder="Select Dependents...")

MultipleLines_option = ({'Yes':1,'No':0, 'No phone service':2})
MultipleLines = col5.selectbox('Multiple Lines', list(MultipleLines_option.keys()),index=None, placeholder="Select Partner...")

InternetService_option = ({'Fiber optic':[0,1,0],'DSL':[1,0,0], 'No':[0,0,1]})
InternetService = col6.selectbox('Internet Service', list(InternetService_option.keys()),index=None, placeholder="Select MultipleLines...")

OnlineSecurity_option = ({'Yes':1,'No':0, 'No internet service':2})
OnlineSecurity = col4.selectbox('Online Security', list(OnlineSecurity_option.keys()),index=None, placeholder="Select Partner...")

OnlineBackup_option =({'Yes':1,'No':0, 'No internet service':2})
OnlineBackup = col5.selectbox('Online Backup', list(OnlineBackup_option.keys()),index=None, placeholder="Select OnlineSecurity...")

DeviceProtection_option =({'Yes':1,'No':0, 'No internet service':2})
DeviceProtection = col6.selectbox('Device Protection', list(DeviceProtection_option.keys()),index=None, placeholder="Select DeviceProtection...")

TechSupport_option = ({'Yes':1,'No':0, 'No internet service':2})
TechSupport = col4.selectbox('Tech Support', list(TechSupport_option.keys()),index=None, placeholder="Select TechSupport...")

StreamingTV_option = ({'Yes':1,'No':0, 'No internet service':2})
StreamingTV = col5.selectbox('StreamingTV', list(StreamingTV_option.keys()),index=None, placeholder="Select StreamingTV...")

StreamingMovies_option = ({'Yes':1,'No':0, 'No internet service':2})
StreamingMovies = col6.selectbox('Streaming Movies', list(StreamingMovies_option.keys()),index=None, placeholder="Select StreamingMovies...")

st.subheader("Billing")
col7,col8,col9 =st.columns([1,1,1])

Contract_option = ({'Month-to-month':0,'One year':1, 'Two year':2})
Contract = col7.selectbox('Contract', list(Contract_option),index=None, placeholder="Select Contract...")

PaperlessBilling_option = ({'Yes':1,'No':0})
PaperlessBilling = col8.selectbox('Paperless Billing:',list(PaperlessBilling_option.keys()),index=None, placeholder="Select PaperlessBilling...")

PaymentMethod_option = ({'Bank transfer':[1,0,0,0], 
                         'Credit card'  :[0,1,0,0],
                         'Electronic check':[0,0,1,0],
                         'Mailed check'    :[0,0,0,1]})
PaymentMethod = col9.selectbox('Payment Method', list(PaymentMethod_option.keys()),index=None, placeholder="Select PaymentMethod...")

MonthlyCharges = col7.number_input('Monthly Charges', min_value = 18, max_value = 120,value =18)
TotalCharges = col8.number_input('Total Charges', min_value= 18, max_value=8685, value =18)

tenure_group_option = ({'1-12' :[1,0,0,0,0,0,0,0],
                        '13-24':[0,1,0,0,0,0,0,0],
                        '25-36':[0,0,1,0,0,0,0,0],
                        '37-48':[0,0,0,1,0,0,0,0],
                        '49-60':[0,0,0,0,1,0,0,0],
                        '61-72':[0,0,0,0,0,1,0,0],
                        '73-84':[0,0,0,0,0,0,1,0],
                        '85-96':[0,0,0,0,0,0,0,1]})
tenure_group = col9.selectbox('tenure_group',list(tenure_group_option.keys()),index=None, placeholder="Select tenure_group...")







col4,col5,col6 =st.columns([1,2,1])
if col5.button(':red[Predict]',use_container_width = True):
    encode = []
    encode.append(SeniorCitizen_option[SeniorCitizen])
    encode.append(partner_option[Partner])
    encode.append(Dependents_option[Dependents])
    encode.append(PhoneService_option[PhoneService])
    encode.append(MultipleLines_option[MultipleLines])
    encode.append(OnlineSecurity_option[OnlineSecurity])
    encode.append(OnlineBackup_option[OnlineBackup])
    encode.append(DeviceProtection_option[DeviceProtection])
    encode.append(TechSupport_option[TechSupport])
    encode.append(StreamingTV_option[StreamingTV])
    encode.append(StreamingMovies_option[StreamingMovies])
    encode.append(Contract_option[Contract])
    encode.append(PaperlessBilling_option[PaperlessBilling])
    encode.append(MonthlyCharges)
    encode.append(TotalCharges)
    for i in InternetService_option[InternetService]:
        encode.append(i)
    for i in PaymentMethod_option[PaymentMethod]:
        encode.append(i)
    for i in tenure_group_option[tenure_group]:
        encode.append(i)
    



    file_path = ('C:/Users/Gowtham/Datascience/telecom_customer_churn/telecom_model.sav')
    
    load = pickle.load(open(file_path,'rb'))
    
    pred = load.predict([encode])
    
    if pred == 1:        
        col5.warning("Customer will Churn")
    elif pred == 0:
        col5.success("Customer will not Churn")
    else:
        pass
    
    