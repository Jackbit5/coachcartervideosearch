import streamlit as st
from streamlit_extras.mention import mention
from streamlit_extras.stylable_container import stylable_container

st.set_page_config(
    page_title="Coach Carter Driving School",
    page_icon="🚗",
)


def timestamp_to_seconds(timestamp):
    """
    Convert a timestamp from HH:MM:SS,MMM format to total seconds.

    :param timestamp: The timestamp string.
    :return: Total seconds as a float.
    """
    hours, minutes, seconds_milliseconds = timestamp.split(":")
    seconds, milliseconds = seconds_milliseconds.split(",")
    total_seconds = (
        int(hours) * 3600 + int(minutes) * 60 + int(seconds) + int(milliseconds) / 1000
    )
    return total_seconds


def find_word_in_srt_seconds(filename, word):
    """
    Search for a word in an SRT file and return the start time in seconds for subtitles containing that word.

    :param filename: The path to the SRT file.
    :param word: The word to search for.
    :return: A list of start times in seconds where the word was found.
    """
    start_times = []
    with open(filename, "r", encoding="utf-8") as file:
        content = file.readlines()

    current_start_time = 0
    for line in content:
        # Check if the line contains a timestamp
        if "-->" in line:
            # Extract and convert the start timestamp to seconds
            start_timestamp = line.split(" --> ")[0]
            current_start_time = timestamp_to_seconds(start_timestamp)
        elif word.lower() in line.lower():
            start_times.append(current_start_time)

    return start_times


st.title("Coach Carter Driving School")
st.divider()

st.write(
    """This is an website that allows you to search for key words within Coach Carter
    instruction videos, helping you to learn about key driving concepts to aid your 
    journey in learning to drive."""
)

st.write("")


st.subheader("**Enter your key word in the box below:**")

key_word = st.text_input("", max_chars=20, placeholder="Write here...")

st.write("")  # for white space

if key_word:

    file = "New-Camera-Angle.srt"
    start_times_list = find_word_in_srt_seconds(file, key_word)

    container = st.container(border=True)

    with container:

        for start_time in start_times_list:

            with stylable_container(
                key=f"container_with_border_{start_time}",
                css_styles="""
                        {
                            border: 1px solid rgba(49, 51, 63, 0.2);
                            border-radius: 1rem;
                            padding: calc(2em - 1px);
    
                        }
                        """,
            ):

                st.video(
                    f"https://www.youtube.com/watch?v=sEC5lTD9SLA&ab_channel=CoachCarter={start_time}"
                )


col1, col2 = st.columns(2)

with col1:
    mention(
        label="Click here to find us on Facebook!",
        icon="",  # Some icons are available... like Streamlit!
        url="https://www.facebook.com/CoachCarterUK",
    )

with col2:
    mention(
        label="Click here to find us on instagram",
        icon="",  # Some icons are available... like Streamlit!
        url="https://www.instagram.com/p/C2KxN_WMMIe/?fbclid=IwAR3sI1L3rRtWn7uf1O_aCQ9v973jXTgYyRvWFkTnjRGSqA5_PfHofDuYPxI",
    )
