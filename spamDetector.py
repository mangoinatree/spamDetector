import pickle 
import streamlit as st

model=pickle.load(open("model.pkl", "rb"))
cv=pickle.load(open("cv.pkl", "rb"))

def main():
    st.title("Email Spam Detector")
    st.subheader("Built with Streamlit & Python")
    msg=st.text_input("Enter email body: ")
    if st.button("Predict"):
        data=[msg]
        vect=cv.transform(data).toarray()
        prediction=model.predict(vect)
        result=prediction[0]

        if result == 1:
            st.error("This is spam mail")
        else:
            st.success("This is ham mail")

if __name__ == "__main__":
    main()