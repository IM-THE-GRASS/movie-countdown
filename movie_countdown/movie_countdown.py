"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
import requests
import json
from datetime import datetime
from rxconfig import config


class State(rx.State):
    times:dict[str, str] = {"Days":"20", "Hours":"11", "Minutes":"23", "Seconds":"34"}
    overview:str
    title:str
    type:str
    release_date:str
    img_url:str
    def get_data(self):
        response = requests.get("https://whenisthenextmcufilm.com/api")
        data = json.loads(response.text)
        self.title = data["title"]
        self.overview = data["overview"]
        self.type = data["type"]
        self.release_date = data["release_date"]
        self.times["Days"] = data["days_until"]
        self.img_url = data["poster_url"]
        
    def update_time(self, _):
        if not self.release_date:
            print("no rel date")
            return
        now = datetime.now()
        rel_date = datetime.strptime(self.release_date, "%Y-%m-%d")
        time_diff = rel_date- now
        hours = time_diff.seconds // 3600#this part
        minutes = (time_diff.seconds % 3600) // 60#and this
        seconds = time_diff.seconds % 60# and thsi were done  by ai
        if hours <10:
            hours = "0" + str(hours)
        if minutes <10:
            minutes = "0" + str(minutes)
        if seconds <10:
            seconds = "0" + str(seconds)
        self.times["Hours"] = str(hours)
        self.times["Minutes"] = str(minutes)
        self.times["Seconds"] = str(seconds)

def countdown_timer(info):
    return rx.vstack(
        rx.text(
            info[1],
            font_weight="bold",
            line_height="7vh",
            letter_spacing="-0.2vw",
            font_size="13vh",
            text_align="center",
            font_family="Roboto"
        ),
        rx.text(
            info[0],
            font_weight="bold",
            line_height="2.6vh",
            letter_spacing="0vw",
            font_size="4vh",
            text_align="center",
            font_family="Roboto",
            width="100%"
        )
    )
@rx.page(on_load=State.get_data())
def index() -> rx.Component:
    return rx.center(
        rx.box(
            
            rx.vstack(
                rx.image(
                    src=State.img_url,
                    width="100%",
                    height="60vh",
                    object_fit="contain"
                ),
                rx.box(
                    rx.hstack(
                        rx.vstack(
                            rx.text(
                                State.title,
                                text_align="start",
                                font_size="2.612vh",
                                letter_spacing="-0.1vw",
                                line_height="2.612vh",
                                font_family="Roboto"
                            ),
                            rx.text(
                                State.overview,
                                font_size="2vh",
                                letter_spacing="1px",
                                line_height="2.2vh",
                                color="E7E0EC",
                                font_family="Roboto",
                                height="15vh"
                            )
                        ),
                        rx.hstack(
                            rx.text(
                                State.release_date,
                                font_size="2vh",
                                letter_spacing="1px",
                                line_height="2.2vh",
                                text_align="end",
                                color="E7E0EC",
                                height="5.5vh",
                                font_family="Roboto"
                            ),
                            rx.text(
                                " ・ ",
                                font_size="2vh",
                                letter_spacing="1px",
                                line_height="2.2vh",
                                text_align="end",
                                color="E7E0EC",
                                height="5.5vh",
                                font_family="Roboto",
                                text_wrap="nowrap"
                            ),
                            rx.text(
                                State.type,
                                font_size="2vh",
                                letter_spacing="1px",
                                line_height="2.2vh",
                                text_align="end",
                                color="E7E0EC",
                                height="5.5vh",
                                font_family="Roboto",
                                text_wrap="nowrap"
                            ),
                            spacing="0"
                        ),
                        justify_content="space-between",
                        width="42vw"
                    ),
                    rx.hstack(
                        rx.foreach(
                            State.times,
                            countdown_timer
                        ),
                        justify_content="space-around",
                        width="42vw",
                        height="100%"
                    ),
                    width="42vw",
                    height="25vh"
                ),
            ),
            width="42vw",
            height="95vh"
        ),
        rx.moment(
            left="1000vw",
            position="absolute",
            interval=1000,
            on_change=State.update_time(),
            display = "none"
        ),
        width="100vw",
        height="100vh",
        overflow="hidden",
    )


app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap",
    ],
)
app.add_page(index)
