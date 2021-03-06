from porthole import GenericReport, QueryExecutor


def main():
    report = GenericReport(
        report_name='sample_report',
        report_title="US Geography - Top Cities"
    )
    report.build_file()
    with QueryExecutor(db="DemoDB") as exec:
        result = exec.execute_query(
            filename="top_cities_by_population",
            params={"population_threshold": 500000}
        )
    report.make_worksheet(
        sheet_name="Top Cities",
        query_results=result
    )
    top_city_name = result.result_data[0]["City Name"]
    top_city_pop = result.result_data[0]["Est. Population (2017)"]
    report.get_recipients()
    report.subject = "Sample Report 3: US Geography - Top Cities by Population"
    report.message = f"""Attached is a list of US cities with populations of more than 500,000. There
are { result.result_count } cities meeting this criteria. The top city is
{ top_city_name }, with a population of { top_city_pop }.
"""
    report.execute()
