from fastapi import FastAPI, APIRouter, Depends, HTTPException
from fastapi.responses import HTMLResponse
from typing import List
import os

# Import the necessary models
from app.models.bank_statement import BankStatement, BankOperation
from app.database import get_db

router = APIRouter(prefix="/bank", tags=["Bank Statements UI"])

@router.get("/statements", response_class=HTMLResponse)
async def get_bank_statements_page():
    """
    Render the bank statements page with options for different banks.
    """
    # This will be expanded to include actual UI rendering
    html_content = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Выписки банка</title>
        <meta charset="utf-8">
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            .bank-selector { margin-bottom: 20px; }
            .bank-option { display: inline-block; margin-right: 15px; }
            .soon { color: #999; }
            .statement-section { border: 1px solid #ccc; padding: 15px; margin-top: 20px; }
        </style>
    </head>
    <body>
        <h1>Выписки банка</h1>
        
        <div class="bank-selector">
            <h2>Выберите банк:</h2>
            <div class="bank-option">
                <input type="radio" id="alfa-bank" name="bank" value="alfa-bank" checked>
                <label for="alfa-bank">Альфа-Банк</label>
            </div>
            <div class="bank-option">
                <input type="radio" id="sber" name="bank" value="sber">
                <label for="sber">Сбер</label>
                <span class="soon">(Скоро)</span>
            </div>
            <div class="bank-option">
                <input type="radio" id="t-bank" name="bank" value="t-bank">
                <label for="t-bank">Т-Банк</label>
                <span class="soon">(Скоро)</span>
            </div>
        </div>
        
        <div id="statement-section" class="statement-section">
            <h2>Импорт выписки Альфа-Банка</h2>
            <p>Выберите PDF файл выписки для импорта:</p>
            <form id="import-form" enctype="multipart/form-data">
                <input type="file" id="pdf-file" name="pdf-file" accept=".pdf" required>
                <br><br>
                <button type="submit">Импортировать</button>
            </form>
            
            <div id="import-result"></div>
        </div>
        
        <script>
            // Simple form handling
            document.getElementById('import-form').addEventListener('submit', function(e) {
                e.preventDefault();
                const fileInput = document.getElementById('pdf-file');
                if (fileInput.files.length > 0) {
                    // In a real implementation, this would submit to backend API
                    document.getElementById('import-result').innerHTML = 
                        '<p>Файл ' + fileInput.files[0].name + ' готов к импорту.</p>';
                }
            });
        </script>
    </body>
    </html>
    '''
    return html_content

@router.get("/statements/{statement_id}", response_class=HTMLResponse)
async def get_statement_page(statement_id: int):
    """
    Render a specific statement page.
    """
    # This will be expanded to show detailed statement information
    html_content = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Выписка банка</title>
        <meta charset="utf-8">
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            table {{ border-collapse: collapse; width: 100%; }}
            th, td {{ border: 1px solid #ccc; padding: 8px; text-align: left; }}
            th {{ background-color: #f2f2f2; }}
        </style>
    </head>
    <body>
        <h1>Выписка банка</h1>
        <p><strong>ID:</strong> {statement_id}</p>
        
        <h2>Информация о выписке</h2>
        <p>Информация будет отображаться здесь</p>
        
        <h2>Операции</h2>
        <table>
            <tr>
                <th>Дата</th>
                <th>Код</th>
                <th>Описание</th>
                <th>Сумма</th>
            </tr>
            <tr>
                <td colspan="4">Данные операций будут отображаться здесь</td>
            </tr>
        </table>
    </body>
    </html>
    '''
    return html_content