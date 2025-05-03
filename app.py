import streamlit as st


def main():
    st.title('Square Calculator')
    st.header('Calculate the square of a number')
    st.subheader('Enter a number to calculate its square')

    input_num = st.number_input('Input a number', value=0)

    result = input_num ** 2
    st.write(f'The square of {input_num} is {result}')


if __name__ == '__main__':
    main()
