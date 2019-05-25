from porthole import BasicReport, QueryExecutor, ResultFilter


def main():
    report = BasicReport(
        report_title="US Geography - Counties by State"
    )
    report.build_file()
    with QueryExecutor(db="DemoDB") as exec:
        result = exec.execute_query(filename="counties_and_subdivision_counts")
    report.make_worksheet(
        sheet_name="All States",
        query_results=result
    )
    by_state = ResultFilter(result_to_filter=result, filter_by="state_name")
    by_state.filter()
    for state, data in by_state:
        report.make_worksheet(
            sheet_name=state,
            query_results=data
    )
    report.to_recipients = ['william.mcmonagle@ankura.com']
    report.cc_recipients = [
        'edward.nunes@ankura.com',
        'shane.metzger@ankura.com',
        'chase.hudson@ankura.com'
    ]
    report.subject = "Sample Report 2: US Geography - Counties by State"
    report.message = "Please find the sample report attached."
    report.execute()
