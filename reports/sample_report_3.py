from porthole import BasicReport, QueryExecutor


def main():
    report = BasicReport(
        report_title="US Geography - Top Cities"
    )
    report.build_file()
    with QueryExecutor(db="DemoDB") as exec:
        result = exec.execute_query(filename="top_cities_by_population")
    report.make_worksheet(
        sheet_name="Top Cities",
        query_results=result
    )
    top_city_name = result.result_data[0]["City Name"]
    top_city_pop = result.result_data[0]["Est. Population (2017)"]
    report.to_recipients = ['william.mcmonagle@ankura.com']
    report.cc_recipients = [
        'edward.nunes@ankura.com',
        'shane.metzger@ankura.com',
        'chase.hudson@ankura.com'
    ]
    report.subject = "Sample Report 3: US Geography - Top Cities by Population"
    report.message = f"""Attached is a list of US cities with populations of more than 500,000. There
are { result.result_count } cities meeting this criteria. The top city is
{ top_city_name }, with a population of { top_city_pop }.
"""
    report.execute()
