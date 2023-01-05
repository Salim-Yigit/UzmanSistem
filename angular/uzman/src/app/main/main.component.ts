import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent {

  inp: string = ""
  trained: boolean = false
  prediction: string = ""
  export_graph: any
  export_heatmap: any

  constructor(private http: HttpClient) {}

  onClickSend() {
      this.http.get<any>(`http://127.0.0.1:5000/prediction/${this.inp}`)
      .subscribe(response => {
        this.trained = true
        this.prediction = response.body 
      }, error => {
        
        this.trained = true
        
        this.prediction = error.error.text
      })
  }

  onClickSendGraph() {
    this.http.get<any>(`http://127.0.0.1:5000/export_graph`)
    .subscribe(response => {
      this.trained = true
      this.export_graph = response.body 
    }, error => {
      
      this.trained = true
      
      this.export_heatmap = error.error.text
    })
  }

  onClickSendHeatmap() {
    this.http.get<any>(`http://127.0.0.1:5000/plot`)
    .subscribe(response => {
      this.trained = true
      this.export_heatmap = response.body 
    }, error => {
      
      this.trained = true
      
      this.export_heatmap = error.error.text
    })
  }

  onKey(event: any) { this.inp = event.target.value;}
}
