import pretty_midi
import collections

def parse_midi_file(midi_file_path):
    """
    Lê um arquivo MIDI e extrai uma lista de notas e suas durações.

    Args:
        midi_file_path (str): O caminho para o arquivo .mid.

    Returns:
        tuple: Uma tupla contendo duas listas: (notes, durations).
               'notes' é uma lista de nomes de notas (ex: 'C4').
               'durations' é uma lista de durações em segundos.
    """
    try:
        midi_data = pretty_midi.PrettyMIDI(midi_file_path)
        notes = []
        
        # Itera sobre todos os instrumentos no arquivo MIDI
        for instrument in midi_data.instruments:
            # Não processa bateria
            if instrument.is_drum:
                continue
            
            # Itera sobre todas as notas do instrumento
            for note in instrument.notes:
                note_name = pretty_midi.note_number_to_name(note.pitch)
                start_time = note.start
                end_time = note.end
                duration = end_time - start_time
                notes.append({
                    'name': note_name,
                    'start': start_time,
                    'duration': duration
                })
        
        # Ordena as notas pelo tempo de início
        sorted_notes = sorted(notes, key=lambda x: x['start'])
        
        note_names = [n['name'] for n in sorted_notes]
        note_durations = [n['duration'] for n in sorted_notes]
        
        return note_names, note_durations

    except Exception as e:
        print(f"Erro ao processar o arquivo MIDI: {e}")
        return None, None