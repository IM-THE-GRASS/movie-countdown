"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.center(
        rx.box(
            
            rx.vstack(
                rx.image(
                    src="https://http.cat/301",
                    width="100%",
                    height="60vh"
                ),
                rx.box(
                    rx.hstack(
                        rx.vstack(
                            rx.text(
                                "This is the name of the movie",
                                text_align="start",
                                font_size="24px",
                                letter_spacing="-2px",
                                line_height="24px"
                            ),
                            rx.text(
                                "This is where the overview will go",
                                font_size="14px",
                                letter_spacing="0.25px",
                                line_height="20px",
                                color="E7E0EC"
                            )
                        ),
                        rx.box(
                            rx.text(
                                "xxxx-xx-xx ・ Movie",
                                font_size="14px",
                                letter_spacing="0.25px",
                                line_height="20px",
                                text_align="end",
                                color="E7E0EC",
                                height="5.5vh"
                            )
                        ),
                        justify_content="space-between",
                        width="42vw"
                    ),
                    width="42vw",
                    height="25vh"
                )
            ),
            width="42vw",
            height="85vh"
        ),
        width="100vw",
        height="100vh",
        overflow="hidden",
    )


app = rx.App()
app.add_page(index)
