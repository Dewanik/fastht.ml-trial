from fasthtml.common import *
app, rt = fast_app()
@rt("/")
def get():
    return(
        Head(
            Title("Welcome to Yantra Inc"),
            Meta(charset="UTF-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1"),
            Link(rel="stylesheet", href="styles.css")
        ),
        Body(
            Header(
                H1("Welcome to Yantra Inc"),
                Nav(
                    Ul(
                        Li(A(P("Home"),href="/", _t="Home")),
                        Li(A(P("Contact"),href="/contact", _t="Contact")),
                        Li(A(P("Services"),href="/services", _t="Services"))
                    )
                )
            ),
            Main(
                H2("Your Trusted Partner in Software Development and Digital Marketing"),
                P("At Yantra Inc, we specialize in delivering high-quality software development, digital marketing, and website development services. Our team of experts is dedicated to providing solutions that drive your business forward."),
                Img(src="images/hero.jpg", alt="Hero Image")
            ),
            Footer(
                P("© 2024 Yantra Inc. All rights reserved.")
            )
    ))
@rt('/contact')

def get():
    return (
        Head(
            Title("Contact Us - Yantra Inc"),
            Meta(charset="UTF-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1"),
            Link(rel="stylesheet", href="styles.css")
        ),
       

                
                H1("Contact Us"),
               
                    Ul(
                        Li(A(P("Home"),href="/", _t="Home")),
                        Li(A(P("Contact"),href="/contact", _t="Contact")),
                        Li(A(P("Services"),href="/services", _t="Services"))
                    ),
            Main(
                H2("We'd Love to Hear from You"),
                P("Have questions or need assistance? Reach out to us using the contact form below or through our contact details."),
                Form(
                    action="/submit_contact",
                    method="post",
                    children=[
                        Label(for_="name", _t="Name"),
                        Input(type="text", id="name", name="name", required=True),
                        Label(for_="email", _t="Email"),
                        Input(type="email", id="email", name="email", required=True),
                        Label(for_="message", _t="Message"),
                        Textarea(id="message", name="message", required=True),
                        Button(type="submit", _t="Submit")
                    ]
                )
            ),
            Footer(
                P("© 2024 Yantra Inc. All rights reserved.")
            )
    )

@rt("/services")
def get():
    return (
        Head(
            Title("Our Services - Yantra Inc"),
            Meta(charset="UTF-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1"),
            Link(rel="stylesheet", href="styles.css")
        ),
        Body(
            Header(
                H1("Our Services"),
                Nav(
                    Ul(
                      Li(A(P("Home"),href="/", _t="Home")),
                        Li(A(P("Contact"),href="/contact", _t="Contact")),
                        Li(A(P("Services"),href="/services", _t="Services"))
                    )
                )
            ),
            Main(
                H2("What We Offer"),
                P("Yantra Inc offers a wide range of services to help your business succeed in the digital world."),
                Ul(
                    Li(
                        H3("Software Development"),
                        P("Custom software solutions tailored to your business needs.")
                    ),
                    Li(
                        H3("Digital Marketing"),
                        P("Effective digital marketing strategies to enhance your online presence.")
                    ),
                    Li(
                        H3("Website Development"),
                        P("Professional website development services to create a strong online foundation.")
                    )
                )
            ),
            Footer(
                P("© 2024 Yantra Inc. All rights reserved.")
            )
    ))

@app.get("/greet/{nm}")
def greet(nm:str):
    return f"Good day to you, {nm}!"


serve()
