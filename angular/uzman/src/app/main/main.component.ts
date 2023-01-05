import {Component} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {DomSanitizer} from "@angular/platform-browser";

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent {

  inp: string = ""
  sendHeatmap: boolean = false
  predicted: boolean = false;
  prediction: string = ""
  
  precision: string = ""
  recall: string = ""
  auc: string = ""
  f1: string = ""

  exported_heatmap: any

  constructor(private http: HttpClient, private sanitizer: DomSanitizer) {
  }

  onClickSend() {
    this.http.get<any>(`http://127.0.0.1:5000/prediction/${this.inp}`)
      .subscribe(response => {
        this.prediction = response.body
        this.predicted = true;
      }, error => {
        this.predicted = true;
        this.prediction = error.error.text
      })
  }

  onClickSendGraph() {
    this.http.get<any>(`http://127.0.0.1:5000/export_graph`)
      .subscribe(response => {
        this.precision = response.precision
        this.recall = response.recall
        this.auc = response.auc
        this.f1 = response.f1
      }, error => {
      })
  }

  onClickSendHeatmap() {
    this.http.get("http://127.0.0.1:5000/plot", {responseType: 'blob'})
      .subscribe(response => {
        const file = new Blob([response], {type: 'image/png'});
        this.exported_heatmap = this.sanitizer.bypassSecurityTrustUrl(URL.createObjectURL(file));
        this.sendHeatmap = true
      });
  }

  onKey(event: any) {
    this.inp = event.target.value;
  }
}