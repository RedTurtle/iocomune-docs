# io-Prenoto

<!--- -----------------------------------------------------------------
  Esempio:
  ---------------------------------------------------------------------

## Versione 7.10.9 (12/09/2023)

### Migliorie

- Fissato il layout di stampa per pagine con Accordion

### Novità

- Nuovo blocco "Informazioni" [`Istruzioni`](https://docs.google.com/document/d/1SThuxa_ah0BuNXukWs564kKPfprK41WLQE8Mome-0xg/edit#heading=h.7ty110jumgmd)

### Fix

- il numero di telefono dentro card ufficio adesso è visibile anche senza indirizzo
-->

<!--- -----------------------------------------------------------------
 TEMPLATE PER RELEASE
 ----------------------------------------------------------------------

## Versione X.X.X (dd/mm/yyyy)

### Migliorie

- ...

### Novità

- ...  [`Istruzioni`](url della documentazione relativa alla novità)

### Fix

- ...
 -->

## Versione 2.6.0 (03/02/2025)

### Migliorie

- A11Y - Aggiunta modale di spostamento prenotazione/blocco da tastiera per l'accessibilità, sia su vista calendario che ricerca lato operatore.
- A11Y - Migliorata l'accessibilità del campo di ricerca per data nella vista calendario
- A11y - Navigazione da tastiera: ora premendo il tasto 'Enter' oppure 'Spazio' è possible aprire una prenotazione.
- A11Y - Navigazione da tastiera: rimossi i pulsanti di 'Aggiungi prenotazione' negli slot già occupati.
- A11y - Migliorata l'accessibilità nella vista elenco e nella modale di cambio di stato.
- A11y - Migliorata l'accessibilità per la form di ricerca del primo slot disponibile.

## Versione 2.5.0 (24/01/2025)

### Migliorie

- Migliorata l'accessibilità delle prenotazioni nella vista a slot: è stata aggiunto allo SR la label per l'ID e il numero di telefono se presente. Inoltre, se è attiva la funzione 'sposta' premendo il tasto 'ESC' si annulla lo spostamento.
- Quando si ricerca il primo slot disponibile, ora compare un pulsante che permette all'utente di spostare il focus sul primo slot disponibile. Migliorata anche l'accessibilità per i non vedenti su questa parte.

### Fix

- Risolto un bug per cui quando si inseriva una prenotazione dal calendario, e subito dopo se ne inseriva una nuova, a volte la tendina con le tipologie di prenotazione era vuota.

### Novità

- Aggiunta la shortcut Alt+Freccia Destra, Alt + Freccia Sinistra per cambiare vista più agevolmente (navigazione fra i tab Ricerca e tab Calendario)

## Versione 2.4.1 (26/11/2024)

- Nella cartella prenotazioni è ora presente la possibilita di configurare gli orari della schedulazione settimanale,
  con la granularita di 5 min, al posto di 15 min nella versione precedente.

## Versione 2.4.0 (07/11/2024)

### Novità

- Nella cartella prenotazioni è ora presente un flag 'Applica le restrizioni sulle date anche agli operatori' che se attivato mostra un messaggio di alert all'operatore nel caso in cui stia tentando di inserire una prenotazione prima del minimi giorni da cui si può effettuare una prenotazione, come già avviene per il campo 'Massimi giorni nel futuro'.

## Versione 2.3.2 (24/10/2024)

### Fix

- Sistemata modale di Cancella prenotazione lato operatore, la dicitura di "notifica all'utente non abilitata via email" ora compare solo se nelle impostazioni della cartella prenotazione viene rimossa la spunta di notifica.

## Versione 2.3.0 (11/10/2024)

### Novità

- Inserita la possibilità di gestire campi personalizzati aggiuntivi, differenti per titpologia, nella
  richiesta di nuove prenotazioni.

## Versione 2.2.8 (21/08/2024)

### Fix

- Sistemata la visualizzazione dell'ufficio dopo la conferma della prenotazione, ora sia indirizzo che contatti si vedono anche su appuntamenti creati dall'operatore.

### Migliorie

- Inserita la possibilità, nella tipologia di prenotazione, di aggiungere un testo di aiuto per il cittadino
  per compilare le informazioni aggiuntive richieste durante la prenotazione.

## Versione 2.2.7 (08/08/2024)

### Migliorie

- Aggiornato dettaglio della prenotazione con annessa Stampa del promemoria sull'orario della prenotazione, ora viene indicato direttamente l'ora dell'appuntamento e non più lo slot che risultava fuorviante per l'utente.

### Fix

- Migliorata la Stampa prenotazioni della vista tabellare della cartella prenotazioni, soprattutto per browser Chrome e Firefox.
- L'indirizzo associato alla stanza di prenotazione adesso viene visualizzato anche quando si viene da link esterno.

## Versione 2.2.5 (31/07/2024)

### Migliorie

- Nell'Area operatore lo `Stampa prenotazioni` ora riporta anche la colonna Dettaglio delle prenotazioni.

## Versione 2.2.4 (25/07/2024)

### Migliorie

- Nello `Stampa promemoria` della prenotazione è stato inserito l'indirizzo dell'ufficio e l'intestazione del sito.

### Fix

- La modale `Messaggi Inviati` dalla vista operatore non dà più errore quando viene modificata una prenotazione.

## Versione 2.2.2 (08/07/2024)

### Fix

- Aggiunte breadcrumbs nella pagina `Le mie prenotazioni`

## Versione 2.2.0 (02/07/2024)

### Novità

- Aggiunto un pulsante di Stampa nella popup di dettaglio di una prenotazione, nella vista operatore

## Versione 1.19.0 (02/04/2024)

### Novità

- Nelle impostazioni di personalizzazione della schedulazione settimanale, ora è possibile definire anche l'anno. In questo modo è possibile quindi chiudere uno sportello in modo ricorrente per un certo periodo.

- Aggiunto nella vista calendario il pulsante per cercare il primo slot disponibile per una certa tipologia di prenotazione.

### Migliorie

- Nella vista calendario dell'operatore, sono stati mostrati degli avvisi nel caso in cui ci si posizioni su una data che supera il numero massimo di giorni nel futuro impostato oppure ci si posizioni su una data non compresa nel range di validità della cartella prenotazioni.

### Fix

- a11y: sistemata l'accessibilità in fase di prenotazione appuntamento

## Versione 1.18.1 (05/03/2024)

### Fix

- Sistemato un bug durante l'inserimento di una prenotazione dal calendario, per cui le disponibilità erano sempre fino a 5 minuti prima della prossima prenotazione o del termine della giornata

- Sistemato un bug durante l'inserimento della prenotazione lato cittadino, per cui se si navigava il sito andando su un servizio differente per prenotare, rimanevano selezionati gli uffici del servizio precedente.

## Versione 1.18.0 (20/02/2024)

### Novità

- le prenotazioni annullate dai cittadini non vengono eliminate completamente, ma rimangono nell'elenco delle prenotazioni
  per gli operatori con lo stato `annullato`.

### Fix

- A11y sistemata accessibilità nella cartella prenotazione, ora dalle breadcrumbs si può passare sulle tab Ricerca/Calendario, migliorata la lettura delle informazioni e la navigabilità nelle tabelle delle postazioni.

### Migliorie

- modificato il messaggio di conferma prenotazione

## Versione 1.17.0 (01/02/2024)

### Novità

- Aggiunto l'ordinamento nella vista ricerca lato Operatore sulle colonne Nome utente e Data prenotazione, l'ordinamento riflette anche sul file csv da scaricare e sull'anteprima di stampa.

## Versione 1.16.0 (26/01/2024)

### Novità

- Inserita la possibilità di modificare le informazioni dell'utente di una prenotazione.
- Aggiunta la possibilità di stampare l'elenco delle prenotazioni.

### Migliorie

- Durante la prenotazione del cittadino, se ci sono delle tipologie non prenotabili, vengono segnalate nel momento in cui viene selezionato un orario per la prenotazione.

### Fix

- Sistemato il pulsante `prenota` nella scheda di servizio, quando la tipologia scelta ha caratteri speciali (lettere accentate, apostrofo, ...). Può essere necessario verificare/riselezionare la tipologia nella modifica del pulsante.

## Versione 1.15.0 (16/01/2024)

### Novità

- Nella vista calendario è stato aggiunto il pulsante 'Oggi' per andare velocemente al calendario della giornata odierna.

### Migliorie

- Quando si passa con il mouse su uno slot disponibile, ora viene visualizzato l'orario in corrispondenza dello slot.
- Migliorata l'accessibilità (a11y) della vista calendario.
- Nella vista tabellare delle prenotazioni, la data di fine di default è stata impostata al giorno corrente, in modo da poter vedere di default in tabella le prenotazioni di oggi.

## Versione 1.14.0 (16/01/2024)

### Migliorie

- Inibita la possibilità di spostare una prenotazione prima di un'altra prenotazione se queste si sovrappongono, o prima del termine della disponibilità oraria se la sua durata eccede la disponibilità oraria.
- Mostrato l'indirizzo dell'ufficio in cui andare nella pagina di riepilogo delle 'Prenotazioni personali' dell'utente.
- Riorganizzate le impostazioni delle notifiche e migliorati i messaggi di default.
- Aggiunta la possibilità di configurare e inviare dei promemoria agli utenti qualche giorno prima della data di prenotazione (necessita di un intervento di RedTurtle per poter funzionare).
- Aggiunta la possibilità di personalizzare il mittente delle mail inviate dalla cartella di prenotazione.

## Versione 1.13.0 (04/01/2024)

- Ora è possibile cancellare una prenotazione all'interno di una Cartella Prenotazioni, tramite l'apposito pulsante nella popup di dettaglio prenotazione.
- Aggiunta data di creazione e ultima modifica nel dettaglio di una prenotazione.

## Versione 1.12.0 (03/01/2024)

### Novità

- Aggiunta l'area personale del cittadino per le prenotazioni ("le mie prenotazioni") dove vengono riepilogate tutte le prenotazioni da lui effettuate, e nella quale può vedere anche lo stato e le comunicazioni relative ad ogni prenotazione.

### Fix

- Sistemata la validazione dei codici fiscali per gli utenti autenticati con SPID (che iniziano con 'tinit-').

## Versione 1.11.0 (19/12/2023)

### Novità

- La durata minima di una tipologia di prenotazione ora è di 5 minuti.
- Aggiunto un campo nella configurazione della Cartella Prenotazione, per confermare automaticamente le prenotazioni create dai gestori (se non è attiva la conferma automatica per tutti). Di base è attivo.

### Migliorie

- Nel pulsante "prenota" della pagina del servizio, ora la scelta della tipologia viene fatta scegliendo da menu a tendina tra le tipologie disponibili, anzichè scrivendo manualmente la descrizione della tipologia.
- Cambiato l'oggetto delle mail inviate ai gestori delle prenotazioni. Ora gli oggetti sono univoci per ogni prenotazione e non vengono raggruppati in thread dai client di posta.
- I gestori possono effettuare prenotazioni senza limitazioni nel futuro (per esempio se si è impostato un limite di giorni nel futuro per fare prenotazioni).

## Versione 1.10.0 (14/12/2023)

### Novità

- Possibilità di gestire sportelli con giorni/orari differenti nelle personalizzazioni delle schedulazioni settimanali. Creando più personalizzazioni per uno stesso intervallo di date, è possibile definire orari diversi per sportelli diversi.
- Aggiunte le briciole di pane nella pagina di prenotazione.

### Fix

- Sistemata vista calendario della Cartella Prenotazione, in particolare il layout degli slot, anche con slot di 5/10 minuti risulta più leggibile e il bottone di spostamento ora è un'icona laterale agli slot.
- Rimosso il menu dalla stampa di riepilogo della prenotazione.

## Versione 1.9.0 (28/11/2023)

### Novità

- Aggiunta del file iCal in allegato anche nelle mail dei gestori della Cartella Prenotazioni.

### Fix

- Sistemato nel dettaglio di una prenotazione sulla vista calendario, il bottone di invio Promemoria, ora appare solo nelle prenotazioni già confermate.
- Nel secondo step della prenotazione, modificata la label "Ufficio" in "Agenda"

## Versione 1.8.3 (20/11/2023)

### Migliorie

- Rimosso il menu dalla stampa di riepilogo della prenotazione.
- Aumentato il limite di durata di una tipologia prenotazione a 180 minuti.
- Data la possibilità al Bookings Manager di creare e spostare prenotazioni e pause.
- Il limite di prenotazioni contemporanee non è più impostato a 2 di default, ma a 0 (illimitato).

### Novità

- Gestione separata delle tipologie di prenotazione. Ora non sono più un campo della Cartella Prenotazioni, ma dei content-type da creare al suo interno. (rif. [Manuale operativo io-Comune](https://docs.google.com/document/d/1BrlGYmE3Z4y6FMIrfBJWOX1P2JVEGzJZS6TRbeIiFSk/edit#heading=h.oc57747u8syu))
  Questa modifica ha il doppio scopo di permettere la creazione di tipologie ad uso interno (lasciandole in stato privato, le possono vedere solo gli operatori)
  e di permettere di specificare delle informazioni aggiuntive (il campo "cosa serve") a seconda della tipologia di prenotazione.
- Aggiunta la variabile per inviare via mail il messaggio di rifiuto della prenotazione (booking_refuse_message).

### Fix

- Migliorata la gestione delle personalizzazioni delle schedulazioni in intervalli temporali a cavallo di un anno (ad esempio da novembre a marzo).
- Migliorata la gestione di eventuali sovrapposizioni di prenotazioni.

## Versione 1.8.1 (3/11/2023)

### Fix

- Sistemato il messaggio di prenotazione confermata al cittadino, nel caso in cui non ci sia la conferma automatica

## Versione 1.8.0 (31/10/2023)

### Migliorie

- Gestito dinamicamente il titolo della pagina finale della prenotazione se nella cartella prenotazione non è stata impostata l'auto-conferma ("Appuntamento confermato", "Appuntamento in attesa di conferma").
- Migliorata la visualizzazione delle prenotazioni brevi nella vista calendario.

### Fix

- Risolti alcuni problemi di ricerca per data delle prenotazioni, nella vista ad elenco.
- Sistemata la visualizzazione di prenotazioni che si sovrappongono alle pause.

## Versione 1.7.1 (30/10/2023)

### Fix

- Risolto un problema nella generazione del calendario appuntamenti quando una prenotazione cade al di fuori degli slot prenotabili.

## Versione 1.7.0 (27/10/2023)

### Migliorie

- Nella validazione del Codice Fiscale del cittadino, ora sono ammessi anche codici fiscali solo numerici a 11 cifre (assegnati tipicamente dall Agenzia delle Entrate).

## Versione 1.6.4

### Migliorie

- Cambiata label "Municipalità" in "Agenda" nel riepilogo della prenotazione.

## Versione 1.6.3

### Novità

- Quando si clicca su 'Sposta' prenotazione dall'elenco delle prenotazioni, implementata la visualizzazione della prenotazione stessa nella vista calendario, per essere direttamente confermata.

## Versione 1.6.0

### Novità

- Aggiunta la possibilità di inviare un messaggio durante il rifiuto di una prenotazione, messaggio che viene allegato alla mail di notifica all'utente.

## Versione 1.5.2

### Fix

- Disabilitato il bottone di invio prenotazione dopo il click, per evitare invii multipli della stessa prenotazione.
