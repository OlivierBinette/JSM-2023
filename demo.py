import datapane as dp

app = dp.App(
    "# ER-Evaluation Demo",
    dp.Select(
        dp.Group(
            dp.Group(
                "## 1 - Predicted Clusterings",
                "PatentsView's Disambiguation History:",
                dp.Attachment(file="Research/JSM-2023/predictions.csv", label="Predicted clusterings"),
            ),
            dp.Group(
                "## 2 - Reference Clustering",
                "Set of 400 hand-disambiguated inventors:",
                dp.Attachment(file="Research/JSM-2023/reference.csv", label="Reference clustering"),
            ),
            dp.Group(
                "## 3 - Sampling Weights",
                "Sampling probability to cluster size:",
                dp.Attachment(file="Research/JSM-2023/weights.csv", label="Sampling weights"),
            ),
            label="Input Data",
            columns=3
        ),
        dp.Group(
            "## Test page 2",
            label="Summary Statistics"
        ),
        dp.Group(
            "## Test pagae 3",
            label="Performance Analysis"
        )
    ),
)


dp.save_report(app, path="demo.html")

