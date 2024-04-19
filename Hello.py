# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import pandas as pd
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="IITM TDS Week 8",
        page_icon="🆘",
        initial_sidebar_state="collapsed",
        menu_items={
        'Report a bug': "https://github.com/4rnv/streamlit-test/issues",
        'About': "Nothing really."
        }
    )
    st.markdown(
    """
    <style>
    [data-testid="collapsedControl"] {
        display: none
    }
    </style>
    """, 
    unsafe_allow_html=True,
    )
    st.write("# IITM TDS Week 8 Assignment")
    st.subheader("Roll No. 22f3002918")
    st.markdown(
        """
        Find the largest of three numbers
    """
    )
    with st.form("Formdesu", clear_on_submit=True):
      n1 = int(st.number_input(label="Enter number 1", step=1, format="%d"))
      n2 = int(st.number_input(label="Enter number 2", step=1, format="%d"))
      n3 = int(st.number_input(label="Enter number 3", step=1, format="%d"))
      state = st.form_submit_button("Enter", type="primary")
      if state:
          if n1 ==0 or n2 ==0 or n3 ==0:
            st.warning("Please enter 3 non-zero numbers")
          else:
            num_list = [n1,n2,n3]
            num_list.sort()
            st.success("{largest} is the largest number".format(largest=num_list[2]))

      user_input = {
        "Value" : [n1, n2, n3],
      }
      df = pd.DataFrame(user_input)
      st.bar_chart(df)

if __name__ == "__main__":
    run()
