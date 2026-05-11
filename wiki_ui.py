from pathlib import Path

import streamlit as st


def show_wiki_image(image_path: Path, width_ratio: float = 0.8) -> None:
    main_col, spacer_col = st.columns([width_ratio, 1 - width_ratio])

    with main_col:
        st.image(image_path, use_container_width=True)
