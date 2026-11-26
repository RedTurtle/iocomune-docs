Per ogni operazione la tabella indica lo stato in cui finisce la pratica, gli stati in cui può passare in seguito e gli eventi che l’operazione genera (✔ = l’evento avviene).

```{container} rt-tabella-compatta

| Operazione | Stato della pratica | Stati possibili in seguito | Messaggio in area personale | Mail al cittadino | Mail agli operatori | Assegnazione ad altri operatori |
|---|---|---|:---:|:---:|:---:|:---:|
| Il cittadino **salva** la pratica in bozza | In bozza | – |  |  |  | <span class="rt-si"><span aria-hidden="true">✔</span><span class="sr-only">Sì</span></span> |
| Il cittadino **finalizza** la pratica | In elaborazione | Sospesa, Annullata, Completata, In bozza | <span class="rt-si"><span aria-hidden="true">✔</span><span class="sr-only">Sì</span></span> | <span class="rt-si"><span aria-hidden="true">✔</span><span class="sr-only">Sì</span></span> | <span class="rt-si"><span aria-hidden="true">✔</span><span class="sr-only">Sì</span></span> | <span class="rt-si"><span aria-hidden="true">✔</span><span class="sr-only">Sì</span></span> |
| L’operatore **assegna** la pratica a un altro operatore | In elaborazione, Annullata, Completata, In bozza | Sospesa, Annullata, Completata, In bozza |  |  | <span class="rt-si"><span aria-hidden="true">✔</span><span class="sr-only">Sì</span></span> | <span class="rt-si"><span aria-hidden="true">✔</span><span class="sr-only">Sì</span></span> |
| L’operatore **sospende** la pratica | Sospesa | In elaborazione, Annullata, Completata, In bozza | <span class="rt-si"><span aria-hidden="true">✔</span><span class="sr-only">Sì</span></span> | <span class="rt-si"><span aria-hidden="true">✔</span><span class="sr-only">Sì</span></span> |  |  |
| L’operatore **annulla** la pratica | Annullata | In bozza | <span class="rt-si"><span aria-hidden="true">✔</span><span class="sr-only">Sì</span></span> | <span class="rt-si"><span aria-hidden="true">✔</span><span class="sr-only">Sì</span></span> |  |  |
| L’operatore **completa** la pratica | Completata | – | <span class="rt-si"><span aria-hidden="true">✔</span><span class="sr-only">Sì</span></span> | <span class="rt-si"><span aria-hidden="true">✔</span><span class="sr-only">Sì</span></span> |  |  |
| L’operatore **riporta in bozza** la pratica[^riporta-in-bozza] | In bozza | – | <span class="rt-si"><span aria-hidden="true">✔</span><span class="sr-only">Sì</span></span> | <span class="rt-si"><span aria-hidden="true">✔</span><span class="sr-only">Sì</span></span> |  | <span class="rt-si"><span aria-hidden="true">✔</span><span class="sr-only">Sì</span></span> |
```

[^riporta-in-bozza]: Riportare una pratica “in bozza” significa, di solito, chiedere al cittadino di integrare o modificare dati che servono all’Ente. Il passaggio allo stato “in bozza” invia comunque un messaggio nell’area personale del cittadino e, contestualmente, una mail al cittadino stesso.
