from .table_style import html_style


class HTMLGenerator:
    def __init__(self, data, headers):
        self.data = data
        self.headers = headers

    def generate_html_table(self):
        """Generate an HTML table with embedded JavaScript for interactivity."""
        html_content = html_style

        # Add table headers
        for header in self.headers:
            html_content += f"<th>{header.capitalize()}</th>"
        html_content += """
                    </tr>
                </thead>
                <tbody>
        """
        # Add table rows
        for row in self.data:
            html_content += "<tr>"
            for cell in row:
                html_content += f"<td>{cell if cell is not None else ''}</td>"
            html_content += "</tr>"
        html_content += """
                </tbody>
            </table>

            <!-- jQuery and DataTables JS -->
            <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
            <script src="https://cdn.datatables.net/1.13.6/js/jquery.dataTables.min.js"></script>
            <script src="https://cdn.datatables.net/buttons/2.2.0/js/dataTables.buttons.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.1.3/jszip.min.js"></script>
            <script src="https://cdn.datatables.net/buttons/2.2.0/js/buttons.html5.min.js"></script>
            <script>
                $(document).ready(function() {
                    $('#referencesTable').DataTable({
                        pageLength: 10,
                        responsive: true,
                        dom: 'Bfrtip',
                        buttons: [
                            'copy', 'csv', 'excel', 'pdf'
                        ],
                        columnDefs: [
                            { targets: 0, width: '20%' },  // Title column width
                            { targets: 1, width: '15%' },  // Authors column width
                            { targets: 2, width: '20%' },  // Topics column width
                            { targets: 3, width: '10%' },  // Type column width
                            { targets: 4, width: '10%' },  // Language column width
                            { targets: 5, width: '25%' }   // Notes column width
                        ],
                        initComplete: function() {
                            // Add search field for each column
                            this.api().columns().every(function() {
                                var column = this;
                                var input = $('<input>')
                                    .appendTo($(column.footer()).empty())
                                    .on('keyup change', function() {
                                        column.search(input.val()).draw();
                                    });
                            });
                        }
                    });
                });
            </script>
        </body>
        <footer style="text-align: center; margin-top: 20px; font-size: 0.9em;">
            <p>Created by Faisal Jayousi</p>
        </footer>
        </html>
        """
        return html_content
