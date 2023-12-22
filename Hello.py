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
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Estralletommm",
        page_icon="🐰",
    )

    st.write("# 🐰Tom个人工具箱")

    st.sidebar.success("工具列表")

    st.markdown(
        """
        生活工作中发现许多细小的点可以通过代码方式搞定，但是又不想通过Java实现那么重的项目。
        用python来实现现这些个人的需求是一个很好的选择。
        框架选择streamlit，刚好试一试新推的社区云部署，简化部署，看看效果如何。\n
        **👈 左边可以选择工具列表进入具体的工具页面**
    """
    )


if __name__ == "__main__":
    run()
