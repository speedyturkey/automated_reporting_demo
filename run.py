from porthole import ReportRunner
from reports import (
    sample_report_1,
    sample_report_2,
    sample_report_3,
    sample_report_4,
    sample_report_5
)

REPORT_MAP = {
    'sample_report_1': sample_report_1.main,
    'sample_report_2': sample_report_2.main,
    'sample_report_3': sample_report_3.main,
    'sample_report_4': sample_report_4.main,
    'sample_report_5': sample_report_5.main,
}


if __name__ == '__main__':
    runner = ReportRunner(REPORT_MAP)
    runner.handle_args()
