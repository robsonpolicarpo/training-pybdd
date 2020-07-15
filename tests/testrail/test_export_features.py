from pathlib import Path

from testrail_ydh.export_testcases import export_testcases


def test_export(request):
    json_sections_path = './tests/testrail/b2b_admin_sections.json'
    feature_path = './tests/backoffice/web/features/acoes_de_vendas/001_campanha_escalonada.feature'

    export_testcases(
        request=request,
        project_name='B2B Admin',
        feature_path=Path(feature_path).absolute(),
        json_section_path=Path(json_sections_path).absolute()
    )
