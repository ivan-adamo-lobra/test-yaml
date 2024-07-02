import yaml

def load_yaml_file(filepath):
    """ Carica un file YAML e restituisce il suo contenuto. """
    with open(filepath, 'r') as file:
        yaml_content = yaml.safe_load(file)
    return yaml_content

def filter_get_methods_and_remove_responses(yaml_content):
    """ Filtra il contenuto YAML per mantenere solo i metodi 'get' e rimuovere le risposte. """
    filtered_content = yaml_content.copy()  # Copia il contenuto originale per preservarlo
    if 'paths' in filtered_content:
        for path in list(filtered_content['paths'].keys()):  # Utilizza list() per evitare modifiche durante l'iterazione
            if 'get' in filtered_content['paths'][path]:
                # Mantieni solo il metodo 'get' per ogni path
                get_details = filtered_content['paths'][path]['get']
                # Rimuovi la sezione 'responses' se presente
                get_details.pop('responses', None)
                filtered_content['paths'][path] = {'get': get_details}
            else:
                # Rimuovi i path che non hanno un metodo 'get'
                del filtered_content['paths'][path]
    return filtered_content

def write_yaml_files(data, base_filename, max_lines=7000):
    """ Scrive i dati filtrati in più file YAML, ciascuno con un massimo di max_lines righe. """
    serialized_data = yaml.dump(data, sort_keys=False, default_flow_style=False)
    lines = serialized_data.splitlines()
    
    file_index = 1
    line_count = 0
    current_file_lines = []
    
    for line in lines:
        if line_count >= max_lines:
            with open(f"{base_filename}_{file_index}.txt", 'w') as file:
                file.write("\n".join(current_file_lines))
            file_index += 1
            line_count = 0
            current_file_lines = []
        
        current_file_lines.append(line)
        line_count += 1
    
    # Scrive l'ultimo file se ci sono linee rimanenti
    if current_file_lines:
        with open(f"{base_filename}_{file_index}.yaml", 'w') as file:
            file.write("\n".join(current_file_lines))

def main():
    yaml_content = load_yaml_file("API_BUSINESS_PARTNER.yaml")
    filtered_content = filter_get_methods_and_remove_responses(yaml_content)
    write_yaml_files(filtered_content, "filtered_output")

if __name__ == "__main__":
    main()
