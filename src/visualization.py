import plotly.express as px

def create_line_chart(data, x, y, title):

    fig = px.line(
        data,
        x=x,
        y=y,
        title=title,
        template="plotly_dark"
    )

    return fig