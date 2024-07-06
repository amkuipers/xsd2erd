import xmlschema


def parse_xsd(xsd_path):
    schema = xmlschema.XMLSchema(xsd_path)
    entities = {}
    relationships = []

    for stype in schema.types.values():
        if stype.is_complex():
            attributes = []
            for subelement in stype.content.iter_elements():
                subelement_type = subelement.type.local_name if not subelement.type.is_complex() else subelement.name
                attributes.append(f"{subelement_type} {subelement.name}")
                # Detect potential relationships from nested elements
                if subelement.type.is_complex():
                    # relationships.append((stype.name, subelement.name))
                    relationships.append((stype.name, subelement.type.name))
            entities[stype.name] = attributes

    for element in schema.elements.values():
        if element.type.is_complex():
            attributes = []
            for subelement in element.type.content.iter_elements():
                subelement_type = subelement.type.local_name if not subelement.type.is_complex() else subelement.name
                attributes.append(f"{subelement_type} {subelement.name}")
                # Detect potential relationships from nested elements
                if subelement.type.is_complex():
                    # relationships.append((element.name, subelement.name))
                    relationships.append((element.name, subelement.type.name))
            entities[element.name] = attributes

    return entities, relationships


def generate_mermaid_erdiagram(entities, relationships):
    er_diagram = "erDiagram\n"
    for entity, attributes in entities.items():
        er_diagram += f"    {entity} {{\n"
        for attribute in attributes:
            er_diagram += f"        {attribute}\n"
        er_diagram += f"    }}\n"

    # Add relationships
    for (parent, child) in relationships:
        er_diagram += f"    {parent} ||--o{{ {child} : contains\n"

    return er_diagram


# convert this XSD
xsd_path = 'books.xsd'
entities, relationships = parse_xsd(xsd_path)
mermaid_code = generate_mermaid_erdiagram(entities, relationships)

# print the ERD of the XSD
print(mermaid_code)
