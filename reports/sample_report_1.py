from porthole import BasicReport


def main():
    report = BasicReport(
        report_title="US Geography - States and Counties"
    )
    report.build_file()
    report.create_worksheet_from_query(
        sheet_name="States",
        query={"filename": "select_states"}
    )
    report.create_worksheet_from_query(
        sheet_name="Counties",
        query={"filename": "select_counties"}
    )
    report.to_recipients = ['william.mcmonagle@ankura.com']
    report.cc_recipients = [
        'edward.nunes@ankura.com',
        'shane.metzger@ankura.com',
        'chase.hudson@ankura.com'
    ]
    report.subject = "Sample Report 1: US Geography - States and Counties"
    report.message = "Please find the sample report attached."
    report.execute()
