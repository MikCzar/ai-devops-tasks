<#
.SYNOPSIS
    Prosty skrypt do backupu bazy danych dla Windows (PowerShell)
#>

$DbName = "app_database"
$BackupDir = "C:\backups\db"  # Ścieżka katalogu w systemie Windows
$Date = Get-Date -Format "yyyyMMdd_HHmmss"
$Filename = Join-Path $BackupDir "${DbName}_${Date}.sql.gz"

# Sprawdź czy katalog istnieje
if (-not (Test-Path $BackupDir)) {
    New-Item -ItemType Directory -Path $BackupDir -Force | Out-Null
    Write-Host "Utworzono katalog $BackupDir"
}

# Wykonaj backup
Write-Host "Rozpoczynam backup bazy $DbName..."

# Uwaga: Do użycia 'gzip' w Windows potrzebujesz zainstalowanego narzędzia (np. z Git for Windows, Cygwin lub GnuWin32)
# oraz dostępności mysqldump i gzip w zmiennej środowiskowej PATH.
& mysqldump -u root -p $DbName | & gzip > $Filename

# W PowerShell dla narzędzi zewnętrznych (takich jak mysqldump) używamy $LASTEXITCODE zamiast $?
if ($LASTEXITCODE -eq 0) {
    Write-Host "Backup zakończony sukcesem: $Filename" -ForegroundColor Green
} else {
    Write-Host "Błąd podczas wykonywania backupu!" -ForegroundColor Red
    exit 1
}