import yaml

def load_yaml_file(filepath):
    """ Carica un file YAML e restituisce il suo contenuto. """
    with open(filepath, 'r') as file:
        yaml_content = yaml.safe_load(file)
    return yaml_content

def filter_get_methods(yaml_content):
    """ Filtra il contenuto YAML per mantenere solo i metodi 'get'. """
    filtered_content = yaml_content.copy()  # Copia il contenuto originale per preservarlo
    if 'paths' in filtered_content:
        for path in list(filtered_content['paths'].keys()):  # Utilizza list() per evitare modifiche durante l'iterazione
            if 'get' in filtered_content['paths'][path]:
                # Mantieni solo il metodo 'get' per ogni path
                get_details = filtered_content['paths'][path]['get']
                filtered_content['paths'][path] = {'get': get_details}
            else:
                # Rimuovi i path che non hanno un metodo 'get'
                del filtered_content['paths'][path]
    return filtered_content

def write_yaml_file(data, filename):
    """ Scrive i dati filtrati in un nuovo file YAML. """
    with open(filename, 'w') as file:
        yaml.dump(data, file, sort_keys=False, default_flow_style=False)

def main():
    yaml_content = load_yaml_file("API_BUSINESS_PARTNER.yaml")
    filtered_content = filter_get_methods(yaml_content)
    write_yaml_file(filtered_content, "filtered_output.yaml")

if __name__ == "__main__":
    main()