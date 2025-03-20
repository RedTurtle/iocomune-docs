# io-Cittadino

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

## Versione 2.5.2 (06/03/2025)

### Migliorie

- Se sono abilittati sia iocittadino che ioprenoto, le prenotazioni che i cittadini fanno da autenticati adottano il principio di
  onceonly per quello che riguarda l'email (attributo email) e il telefono (attributo phone). Quindi se, ad esempio, il cittadino
  da autenticato fa una prenotazione e imposta una email differente, quella email verrà riproposta per le prenotazioni o
  i servizi richiesti successivamente.

## Versione 2.5.1 (25/02/2025)

### Migliorie

- Nella compilazione di una pratica, è stata spostata la popup di notifica salvataggio in bozza nell'angolo destro in alto alla pagina, per permettere all'utente di avere un feedback sul salvataggio, è possibile inoltre chiudere la notifica manualmente o attendere che scompaia in automatico dopo qualche secondo.

### Fix

- Sistemato active sullo step di una pratica che quando veniva salvata in bozza tornava all'inizio degli step invece di rimanere su quello corrente.

## Versione 2.5.0 (24/01/2025)

### Novità

- Aggiunto visualizzazione del protocollo di chiusura di una pratica quando si usa l'integrazione con il protocollo

## Versione 2.4.6 (23/01/2025)

### Fix

- Migliorata la visualizzazione delle descrizione dei campi di input nei form delle pratiche.

## Versione 2.4.5 (18/12/2024)

### Migliorie

- Migliorata visualizzazione delle tab della pratica in versione mobile
- Aggiunto nuovo campo testuale per la gestione del piè di pagina nel PDF generato dalla pratica (rif. [Manuale io-Cittadino](https://docs.google.com/document/d/1WdaihkxjGKni19x4wCN6gqT0NrY8h9OAE8H5AgffY9M/edit?tab=t.0#heading=h.d0i528lauo0s))
- Migliorata la gestione di alcuni campi specifici nella generazione del PDF (ad esempio le parti testuali di disclaimer, i campi radiobutton o check, ed i nomi dei file)
- Gestita la sovrascrittura in onceonly di alcuni dei dati utente che arrivano da SPID/CIE

### Fix

- Fissato il backend (versione 1.1.4) per la gestione del campo checkbox "Altro"

## Versione 2.4.3 (25/11/2024)

### Migliorie

- Modificata la dicitura 'Finalizza la pratica' in 'Completa la pratica'

## Versione 2.4.0 (04/11/2024)

### Migliorie

- Revisione dei messaggi inviati al cambio di stato
- Aggiunto campo nel modello pratica per gestire la "firma" per le email (può essere aggiunto ad esempio un ufficio di contatto
  o un generico messaggio "email automatica non rispondere")
- Restyling del Report PDF della pratica, riportato uffico nel footer, data e numero della pratica

## Versione 2.3.3 (29/08/2024)

### Migliorie

- Nei modelli pratica ora è possibile inserire il numero di giorni per i prossimi passi, al cittadino vengono proposte nel riepilogo
  le date esatte dei prossimi passi. Richiede intervento redazionale nei modelli pratica per sistemare le informazioni inserite.
- Nella pagina di riepilogo ora sono stati aggiunti anche i pulsanti "Indietro" e "Salva bozza".
- Il form di feedback ora ha come titolo "Quanto è stato facile usare questo servizio?" solo dopo che il cittadino ha sottomesso la pratica.
- Nei modelli pratica è possibile definire un operatore di default tra le persone nel gruppo "operatori pratiche", all'operatore
  verranno assegnate automaticamente le pratiche del modello.

## Versione 2.3.2 (28/05/2024)

### Migliorie

- Migliorata la tipografia del pdf generato per le pratiche.
- Aggiunti dati sulla protocollazione quando il pacchetto di integrazione protocolli è attivo.

## Versione 2.3.1 (19/12/2023)

### Migliorie

- Disabilitato il tasto ESC e il click fuori dalla popup della form di configurazione Modello Pratica per evitare di chiudere la modale perdendo le modifiche fatte, inoltre è stato aggiunto un avviso sulla X della modale.

## Versione 2.2.1 (08/11/2023)

### Fix

- Nascosto il campo 'Modello' nella creazione di un nuovo 'Modello pratica'. Il campo sarà visibile solo quando il modello pratica sarà salvato.

## Versione 2.2.0 (15/09/2023)
