import dash_html_components as html
import dash_bootstrap_components as dbc

def Footer():
    footer = html.Footer(
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Img(src="assets/images/logo_black.png", height="70px")
                            ],
                        ),
                        dbc.Col(
                            html.A(
                                    dbc.Row(
                                        [
                                            dbc.Col(html.Img(src="assets/images/mit.png", height="60px")),
                                            dbc.Col(html.Img(src="assets/images/orc.png", height="70px")),
                                        ],
                                        no_gutters=True,
                                    ),
                                    href="https://orc.mit.edu/",
                                 ),
                        ),
                        dbc.Col(
                            [
                                dbc.NavLink("Team", href="/team", style={"fontSize":15,"marginRight":10}),
                                dbc.NavLink("Contact Us", href="/contact", style={"fontSize":15,"marginBottom":0}),
                            ],
                        ),
                    ],
                ),
                id="footer",
            )

    return footer
