"""Valida estructura, no comportamiento en iOS ni firma de Apple."""
import json
from pathlib import Path
import plistlib
import uuid
root=Path(__file__).resolve().parents[1]
catalog=json.loads((root/'catalogo.json').read_text(encoding='utf-8'))
assert len(catalog)==20
assert len({row['id'] for row in catalog})==20
for row in catalog:
    assert (root/row['guia']).is_file()
    assert row['validado_en_ios'] is False
files=list((root/'plantillas-sin-firmar').glob('*.shortcut'))
assert len(files)==6
for path in files:
    value=plistlib.loads(path.read_bytes())
    assert value['WFWorkflowName']
    seen=set()
    def validate_reference(data):
        if isinstance(data,dict):
            if data.get('Type')=='ActionOutput':
                assert data['OutputUUID'] in seen, (path,data)
            for item in data.values(): validate_reference(item)
        elif isinstance(data,list):
            for item in data: validate_reference(item)
    for action in value['WFWorkflowActions']:
        assert action['WFWorkflowActionIdentifier'].startswith('is.workflow.actions.')
        params=action['WFWorkflowActionParameters']
        validate_reference(params)
        uid=params['UUID'];uuid.UUID(uid)
        assert uid not in seen
        seen.add(uid)
    print('Estructura válida (sin prueba iOS):',path.name)
print('20 guías y 6 estructuras comprobadas. Firma e importación pendientes en Apple.')
