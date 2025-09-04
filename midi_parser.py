# midi_parser.py
import pretty_midi

def parse_midi_file(midi_file_path):
    """
<<<<<<< HEAD
<<<<<<< HEAD
    Lê um arquivo MIDI e extrai uma lista de trilhas de instrumentos.
    Cada trilha contém o nome do instrumento, o program number e suas notas/durações.
=======
    Lê um arquivo MIDI e extrai uma lista de notas e suas durações.
    A função também converte a notação de sustenidos (ex: 'C#4') para
    a notação interna do projeto (ex: 'c4').

    Args:
        midi_file_path (str): O caminho para o arquivo .mid.

    Returns:
        tuple: Uma tupla contendo duas listas: (notes, durations).
               'notes' é uma lista de nomes de notas (ex: 'C4', 'c4').
               'durations' é uma lista de durações em segundos.
>>>>>>> 2c3bbd2 (Improves MIDI parsing and note generation)
=======
    Lê um arquivo MIDI e extrai uma lista de trilhas de instrumentos.
    Cada trilha contém o nome do instrumento, o program number e suas notas/durações.
>>>>>>> 69f1097 (Adds multi-instrument MIDI synthesis support)
    """
    try:
        midi_data = pretty_midi.PrettyMIDI(midi_file_path)
        instrument_tracks = []

        for instrument in midi_data.instruments:
            if instrument.is_drum:
                continue

            notes_for_instrument = []
            for note in instrument.notes:
                note_name = pretty_midi.note_number_to_name(note.pitch)
                
<<<<<<< HEAD
<<<<<<< HEAD
                if '#' in note_name:
                    char_note = note_name[0]
                    octave_part = note_name[2:]
                    note_name = char_note.lower() + octave_part
=======
                # --- INÍCIO DA TRADUÇÃO ---
                # Se a nota for um sustenido (contém '#')
=======
>>>>>>> 69f1097 (Adds multi-instrument MIDI synthesis support)
                if '#' in note_name:
                    char_note = note_name[0]
                    octave_part = note_name[2:]
                    note_name = char_note.lower() + octave_part
<<<<<<< HEAD
                # --- FIM DA TRADUÇÃO ---
>>>>>>> 2c3bbd2 (Improves MIDI parsing and note generation)
=======
>>>>>>> 69f1097 (Adds multi-instrument MIDI synthesis support)

                start_time = note.start
                end_time = note.end
                duration = end_time - start_time
                
                # Armazena a nota com seu tempo de início para ordenação
                notes_for_instrument.append({
                    'name': note_name,
                    'start': start_time,
                    'duration': duration
                })
            
            # Só adiciona a trilha se ela tiver notas
            if notes_for_instrument:
                instrument_tracks.append({
                    'name': instrument.name,
                    'program_number': instrument.program,
                    'notes': sorted(notes_for_instrument, key=lambda x: x['start'])
                })
        
        return instrument_tracks

    except Exception as e:
        print(f"Erro ao processar o arquivo MIDI: {e}")
        return []