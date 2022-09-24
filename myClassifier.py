import joblib
import streamlit as st

def noBehavior(it=object):
    for xx in it:
        st.write(xx)


def classif(ite=object,item=object):
    clf = joblib.load('classifier/classifier.pkl')
    preped = item

    resource= clf.predict(preped)[0]
    if resource == 0:
        st.title("The file submitted is: Benign")
    else:
        st.title("The file submitted is: Ransomware")
    st.subheader("Behavior of the tested file...")
    for xx in ite:
        st.write(xx)
