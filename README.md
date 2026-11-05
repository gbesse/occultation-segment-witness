# occultation-segment-witness

## Français

Trouver les liaisons coupées par un corps sphérique.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m occultation_segment_witness examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Calcule distance au segment fermé et intersections sphériques ; distingue un segment d’une droite infinie pour éviter de faux blocages.

### Limites

Géométrie sphérique instantanée en unités communes ; pas d’ellipsoïde, réfraction, terrain ou visibilité orbitale temporelle.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Find links blocked by a spherical body.

Synthetic data; no network access or secret required.

```sh
python -m occultation_segment_witness examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Computes distance to the closed segment and spherical intersections; distinguishes a segment from an infinite line to avoid false blockage.

### Limits

Instantaneous spherical geometry in common units; no ellipsoid, refraction, terrain or temporal orbital visibility.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Encontrar enlaces bloqueados por un cuerpo esférico.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m occultation_segment_witness examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Calcula distancia al segmento cerrado e intersecciones esféricas; distingue segmento de recta infinita para evitar falsos bloqueos.

### Límites

Geometría esférica instantánea en unidades comunes; sin elipsoide, refracción, terreno ni visibilidad orbital temporal.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/cspice/occult_c.html
