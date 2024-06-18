import datapane as dp
import pickle
import plotly

with open("Research/JSM-2023/plot_summaries.pkl", "rb") as file:
    plot_summaries = pickle.load(file)
with open("Research/JSM-2023/plot_comparisons.pkl", "rb") as file:
    plot_comparisons = pickle.load(file)
with open("Research/JSM-2023/plot_performance.pkl", "rb") as file:
    plot_performance = pickle.load(file)

with open("Research/JSM-2023/plot_metrics.pkl", "rb") as file:
    plot_metrics = pickle.load(file)
with open("Research/JSM-2023/plot_fairness.pkl", "rb") as file:
    plot_fairness = pickle.load(file)
with open("Research/JSM-2023/plot_dtree.pkl", "rb") as file:
    plot_dtree = pickle.load(file)

app = dp.App(
    "# ER-Evaluation Demo",
    dp.Select(
        dp.Group(
            dp.Group(
                "## 1 - Predicted Clusterings",
                "PatentsView's Disambiguation History:",
                dp.Attachment(
                    file="Research/JSM-2023/predictions.csv",
                    label="Predicted clusterings",
                ),
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
            columns=3,
        ),
        dp.Select(
            dp.Group(
                "## Disambiguation Summary Statistics",
                dp.Group(
                    dp.BigNumber(
                        heading="Avg. Cluster Size",
                        value="10.79",
                        change="33%",
                        is_upward_change=True,
                    ),
                    dp.BigNumber(
                        heading="Matching Rate",
                        value="97%",
                        change="3%",
                        is_upward_change=True,
                    ),
                    dp.BigNumber(
                        heading="Name Variation Rate",
                        value="25%",
                        change="34%",
                        is_upward_change=True,
                    ),
                    dp.BigNumber(
                        heading="Homonymy Rate",
                        value="20%",
                        change="60%",
                        is_upward_change=False,
                    ),
                    columns=4,
                ),
                plot_summaries,
                label="Summary Statistics",
            ),
            dp.Group(
                "## Pairwise Comparisons",
                plot_comparisons,
                label="Comparison Metrics",
            ),
            label="Summary and Comparison Statistics",
        ),
        dp.Group(
            dp.Select(
                dp.Group(
                    "## Performance Estimates",
                    dp.Group(
                        dp.BigNumber(
                            heading="Precision",
                            value=r"88.3% (3.7%)",
                        ),
                        dp.BigNumber(
                            heading="Recall",
                            value=r"97.7% (1.4%)",
                        ),
                        dp.BigNumber(
                            heading="F-Score",
                            value=r"92.8% (2.1%)",
                        ),
                        columns=3,
                    ),
                    plot_performance,
                    label="Performance Estimates",
                ),
                dp.Group("## Cluster-Wise Error Metrics", plot_metrics, label="Error Metrics"),
                dp.Group(
                    "## Performance Bias",
                    plot_fairness,
                    "## Residual Analysis",
                    plot_dtree,
                    label="Error Analysis",
                ),
                dp.Group(
                    "## Error Auditing",
                    dp.Media(file="Research/JSM-2023/streamlit.png"),
                    label="Error Auditing",
                ),
            ),
            label="Performance Analysis",
        ),
        dp.Group(
            dp.Media(file="Research/JSM-2023/fig_sensitivity.png"),
            label="Sensitivity Analysis",
        ),
    ),
)


dp.save_report(app, path="demo.html")
