from process_dataset import get_dataset
choosen_graph, _ = get_dataset()
def eval_report(choosen_graph):
    result_dict = {
        "choosen_graph": choosen_graph,
        "changed_requirements": 0,
        "cost_analysis": 0,
        "impact_analysis": 0,
        "requirement_analysis": 0,
        "market_analysis": 0,
        "variant_analysis": 0,
    }

    return result_dict