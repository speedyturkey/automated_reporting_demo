from porthole import BasicReport


def main():
    report = BasicReport(
        report_title="US Geography - This One Doesn't Work"
    )
    report.build_file()
    report.create_worksheet_from_query(
        sheet_name="States",
        query={"filename": "select_states"}
    )
    report.create_worksheet_from_query(
        sheet_name="Counties / Etc",
        query={"filename": "select_counties"}
    )
    report.create_worksheet_from_query(
        sheet_name="Doesn't Exist",
        query={"filename": "this_query_doesnt_exist"}
    )
    report.to_recipients = ['william.mcmonagle@ankura.com']
    report.cc_recipients = [
        'edward.nunes@ankura.com',
        'shane.metzger@ankura.com',
        'chase.hudson@ankura.com'
    ]
    report.subject = "Sample Report 4: This One Doesn't Work"
    report.message = "Please find the sample report attached."
    report.execute()
